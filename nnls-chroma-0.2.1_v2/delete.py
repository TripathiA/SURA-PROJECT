# import os, os.path

# for root, _, files in os.walk("C:/Users/HP/Desktop/testing"):
#     for f in files:
#         fullpath = os.path.join(root, f)
#         if os.path.getsize(fullpath) < 200 * 1024:
#             os.remove(fullpath)

import os
import shutil
import subprocess

# Return all files in dir, and all its subdirectories, ending in pattern
def gen_files(dir, pattern):
   for dirname, subdirs, files in os.walk(dir):
      for f in files:
         if f.endswith(pattern):
            yield os.path.join(dirname, f)


# Remove all files in the current dir matching *.config
for f in gen_files("C:/Users/HP/Desktop/nnls-chroma-0.2.1_v2", '.o'):
   os.remove(f)

for f in gen_files("C:/Users/HP/Desktop/nnls-chroma-0.2.1_v2", '.dll'):
   os.remove(f)

build_dir = "C:/Users/HP/Desktop/nnls-chroma-0.2.1_v2"

cwd = os.getcwd() # get current directory
try:
	os.chdir(build_dir)
	os.system("mingw32-make")
finally:
	os.chdir(cwd)

for f in gen_files("C:/Program Files (x86)/Vamp Plugins", '.dll'):
   os.remove(f)

for f in gen_files("C:/Users/HP/Desktop/nnls-chroma-0.2.1_v2", '.dll'):
   shutil.copy(f,"C:/Program Files (x86)/Vamp Plugins" )

# os.system("cmd.exe C:/Program Files (x86)/Sonic Visualiser/Sonic Visualiser.exe")

subprocess.Popen(r"C:/Program Files (x86)/Sonic Visualiser/Sonic Visualiser.exe")

