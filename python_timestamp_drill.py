import shutil
import os
import time
from datetime import timedelta, datetime

source = 'C:/Users/rianjeong/Desktop/Folder_A'
destination = 'C:/Users/rianjeong/Desktop/Folder_B'
now = time.time()
diff_sec = float(24*3600)
before = now - diff_sec
####filesTomove = before.strftime("%d %b %Y %I:%M:%S %p")

for files in os.listdir(source):
    src_file = os.path.join(source, files)
    dst_file = os.path.join(destination, files)
    st = os.stat(src_file)

    mod_time = datetime.fromtimestamp(st.st_mtime)
    new_time = time.mktime(mod_time.timetuple())
    if new_time > before:
        shutil.copy(src_file, dst_file)



    
##    st = datetime.fromtimestamp(time.time())
##    mod_time = time.mktime(st.timetuple())
    #print before

        
                        
    
##    src_file = os.path.join(source, files)
##    dst_file = os.path.join(destination, files)
    
