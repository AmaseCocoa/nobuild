import shutil
import os

from ..livebuild import LiveBuild

from ..utils import calculate_sha256, dump_filename

def step_build(console, lb: LiveBuild, architecture: str, filename: str, name: str, version: str, work_dir: str = "./work") -> bool:
    console.print("Building Distro....")
    lb.build()

    filename = dump_filename(filename, name=name, version=version, arch=architecture)
    
    if os.path.exists(os.path.join(work_dir, f"live-image-{architecture}.hybrid.iso")):
        shutil.move(os.path.join(work_dir, f"live-image-{architecture}.hybrid.iso"), f"./dist/{filename}")
        console.print("Generating hash....")
        with open(f"./dist/{filename}.sha256", "w") as f:
            f.write(calculate_sha256(f"./dist/{filename}"))
        return True
    else:
        console.print('[red]ERR![/red]: Failed to build the image, try running "nobuild cleanup" to remove the previous files.')
        return False