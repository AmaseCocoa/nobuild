import subprocess

debian_versions = {
    "1.1": "buzz",
    "1.2": "rex",
    "1.3": "bo",
    "2": "hamm",
    "2.1": "slink",
    "2.2": "potato",
    "3": "woody",
    "3.1": "sarge",
    "4": "etch",
    "5": "lenny",
    "6": "squeeze",
    "7": "wheezy",
    "8": "jessie",
    "9": "stretch",
    "10": "buster",
    "11": "bullseye",
    "12": "bookworm",
    "13": "trixie",
    "14": "forky",
    "sid": "sid",
    "testing": "testing",
    "stable": "stable"
}

class LiveBuild:
    def __init__(self, cwd: str = "./work", extra: str = ""):
        self.cwd = cwd

        self.extra: str = extra
        self.bootappend_live = "boot=live components"
        self.archive_areas = "main"
        self.arch = "amd64"
        self.version = "bookworm"
        self.bootloaders = "grub-pc grub-efi"
        self.mirror = "http://httpredir.debian.org/debian"

    def set_bootappend_live(self, bootappend: list[str] = ["boot=live", "components"]):
        self.bootappend_live = " ".join(bootappend)

    def set_archive_areas(self, areas: list[str] = ["main"]):
        self.archive_areas = " ".join(areas)

    def set_bootloaders(self, bootloaders: list[str] = ["grub-pc", "grub-efi"]):
        self.bootloaders = " ".join(bootloaders)

    def set_arch(self, arch: str = "amd64"):
        self.arch = arch

    def set_version(self, version: str = "bookworm"):
        self.version = debian_versions.get(version, version)

    def set_mirror(self, mirror: str = "http://httpredir.debian.org/debian"):
        if mirror == "":
            mirror = "http://httpredir.debian.org/debian"
        self.mirror = mirror

    def apply_config(self):
        cmd = f'lb config --distribution "{self.version}" --archive-areas "{self.archive_areas}"'
        cmd += f'--bootloaders "{self.bootloaders}" --bootappend-live "{self.bootappend_live}"'
        cmd += f'--mirror-bootstrap {self.mirror} --mirror-chroot {self.mirror} --mirror-binary {self.mirror} '
        cmd += self.extra
        subprocess.run(cmd, shell=True, cwd=self.cwd)

    def build(self):
        subprocess.run("lb build", shell=True, cwd=self.cwd)

    def clean(self, binary: bool = False):
        subprocess.run(f"lb clean {"--binary" if binary else ""}", shell=True, cwd=self.cwd)
