import gzip
import shutil
import tarfile
import zipfile
import os
import matplotlib.pyplot as plt
import numpy as np

#def archive size function
def archive_size(file):
    size = os.stat(file).st_size
    print "Archive tar: ", size, 'bytes'
    return size
#def archive size function, returns archive name
folder = 'folder'
folder_size = 0
#define folder size function
for (path, dirs, files) in os.walk(folder):
  for file in files:
    filename = os.path.join(path, file)
    folder_size += os.path.getsize(filename)
print "Start folder size: %s bytes" % (folder_size)

#zip, tar, bztar or gztar
def archive_folder(folder, type, name):
    shutil.make_archive(name, type, folder)
    if type == 'bztar':
        return archive_size(name+'.tar.bz2')
    elif type == 'gztar':
        return archive_size(name+'.tar.gz')
    elif type == 'zip':
        return archive_size(name+'.zip')

compression1 = (1-float(archive_folder(folder, 'zip', 'arch'))/float(folder_size))*100
compression2 = (1-float(archive_folder(folder, 'bztar', 'arch'))/float(folder_size))*100
compression3 = (1-float(archive_folder(folder, 'gztar', 'arch'))/float(folder_size))*100
#data
np.random.seed(42)
data = np.random.rand(5)
names = ['zip','bztar','gztar']

ax = plt.subplot(111)
bins = [compression1, compression2, compression3]
print bins
ax.bar(bins, 100)
ax.set_xticks(map(lambda x: x, range(1,len(data)+1)))
ax.set_xticklabels(names,rotation=45)

plt.show()