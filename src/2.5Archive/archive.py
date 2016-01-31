import gzip
import tarfile
import os

#define folder size function
#def archive size function
#def archiver (for diff types of archivers)
# pick a folder you have ...
folder = 'codeacademy'
folder_size = 0
for (path, dirs, files) in os.walk(folder):
  for file in files:
    filename = os.path.join(path, file)
    folder_size += os.path.getsize(filename)
print "%s bytes" % (folder_size)

tar = tarfile.open("Arch.tar.gz", "w:gz")
tar.add("codeacademy", arcname="Arch")
tar.close()

arcinfo = os.stat('Arch.tar.gz').st_size
print arcinfo, 'bytes'


"""
f_in = open('codeacademy')
f_out = gzip.open('box.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()

arcinfo = os.stat('box.gz').st_size
print arcinfo, 'bytes'
"""
