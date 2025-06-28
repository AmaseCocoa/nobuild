import os

from rich.console import Console

from ...config import load_config
from ...types import Config

from .livebuild import LiveBuild

from .step.flavor import copy_flavor_files
from .step.copy_files import copy_files_to_work
from .step.build import step_build

def generate(work_dir: str = "./work", flavor: str | None = None, cache: bool = True):
    console = Console()

    config: Config = load_config()
    version = config['base']['version']
    architecture = config['base']['architecture']
    mirror = config["extra"].get("mirror")
    archive_areas: str = config["extra"].get("archive_areas", "main")

    console.print("nobuild-debian")
    console.print(f"base: {version}-{architecture}")
    os.makedirs("./dist", exist_ok=True)

    lb = LiveBuild(work_dir, config["extra"].get("config_flag", ""))

    if os.path.isdir(work_dir):
        console.print("Old configuration found. reusing...")
        lb.clean(not cache)
    else:
        console.print("Generating live-build configuration...")
        os.makedirs(work_dir, exist_ok=True)

    lb.set_bootloaders(["grub-efi", "grub-pc"])
    lb.set_bootappend_live(["boot=live", "components"])
    lb.set_archive_areas(archive_areas.split(" "))
    lb.set_arch(architecture)
    lb.set_version(version)
    lb.apply_config()
    if mirror:
        lb.set_mirror(mirror)

    copy_files_to_work(work_dir)
    if flavor:
        copy_flavor_files(flavor, work_dir)

    console.print("Building Distro....")
    lb.build()

    result = step_build(console, lb, architecture, config["build"]["filename"], config["main"]["name"], config["main"]["version"], work_dir)
    if result:
        console.print("Done!")