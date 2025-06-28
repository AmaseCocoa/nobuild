import shutil
import os

def copy_extra(source: str = "./src/extra", dist: str = "./work/config"):
    for filename in os.listdir(source):
        source_file = os.path.join(source, filename)
        target_file = os.path.join(dist, filename)
        if os.path.isdir(source_file):
            shutil.copytree(source_file, target_file, dirs_exist_ok=True)
        else:
            shutil.copy2(source_file, target_file)

def copy_files(source: str = "./src/files", dist: str = "./work/config/includes.chroot_after_packages"):
    if os.path.isdir(source):
        for item in os.listdir(source):
            src_path = os.path.join(source, item)
            dst_path = os.path.join(dist, item)
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
            else:
                shutil.copy2(src_path, dst_path)

def copy_repo(source: str = "./src/repo", dist: str = "./work/config/archives/"):
    if os.path.isdir(source):
        for file in os.listdir(source):
            src_file = os.path.join(source, file)
            dst_file = os.path.join(dist, file)

            shutil.copy(src_file, dst_file + ".chroot")        
            shutil.copy(src_file, dst_file + ".binary")