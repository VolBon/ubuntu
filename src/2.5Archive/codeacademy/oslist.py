import glob, os
os.chdir("/python")
for file in glob.glob("*.txt"):
    print(file)
