import shutil
import os

source = 'C:/Users/rianjeong/Desktop/Folder_A'
destination = 'C:/Users/rianjeong/Desktop/Folder_B'



for files in os.listdir(source):
    print os.listdir(source)
    src_file = os.path.join(source, files)
    dst_file = os.path.join(destination, files)
    shutil.move(src_file, dst_file)
