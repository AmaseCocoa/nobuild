import os

from nobuild.pkg import get_package_list

from ..files import copy_files, copy_repo, copy_extra

def copy_files_to_work(work_dir: str = "./work"):
    copy_repo()
    with open(os.path.join(work_dir, "config/package-lists/standard.list.chroot"), "w") as f:
        f.write("! Packages Priority standard")
    with open(os.path.join(work_dir, "config/package-lists/base.list.chroot"), "w") as f:
        f.write("\n".join(get_package_list()))
    copy_files()
    copy_extra()