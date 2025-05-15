import os
import shutil


def copy_files_recursive(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    contents = os.listdir(src)
    for content in contents:
        src_path = os.path.join(src, content)
        dst_path = os.path.join(dst, content)
        
        if os.path.isdir(src_path):
            os.makedirs(os.path.join(dst, content))
            copy_files_recursive(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)
