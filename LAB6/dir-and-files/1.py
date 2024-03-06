import os

directorylist = os.listdir()

for dir in directorylist:
    print(dir)
    print(os.path.isfile)
    print(os.path.isdir)

specified_path = "../built-in-functions/"
print(os.listdir(specified_path))