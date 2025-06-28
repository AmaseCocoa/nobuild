import os

from nobuild.pkg import get_package_list

from ..files import copy_files, copy_repo, copy_extra

def copy_flavor_files(flavor: str, work_dir: str = "./work"):
    copy_repo(f"./src/flavor/{flavor}/repo")
    copy_files(f"./src/flavor/{flavor}/files")
    copy_extra(f"./src/flavor/{flavor}/extra")
    with open(os.path.join(work_dir, f"config/package-lists/{flavor}.list.chroot"), "w") as f:
        f.write("\n".join(get_package_list(f"./src/flavor/{flavor}/packages.nv")))