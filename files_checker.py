from os import listdir
from os.path import isdir, getsize
from sys import platform, argv
from hashlib import md5

if platform.startswith("win"):
    pathc = "\\"
else:
    pathc = "/"
dir_list = []
file_list = []


def ver_dir(path):
    path_downs = listdir(path)
    for i in path_downs:
        a = path + pathc + i
        if isdir(a):
            dir_list.append(path + pathc + i)
            print("dir:", dir_list[-1])
        else:
            file_list.append(path + pathc + i)
            print("file:", file_list[-1])


def get_all_file():
    while True:
        for i in dir_list:
            ver_dir(path=i)
        break

def hashfile(path, algorithm):
    size = getsize(path)
    with open(path, 'rb') as f:
        while size >= 1024 * 1024:
            algorithm.update(f.read(1024 * 1024))
            size -= 1024 * 1024
        algorithm.update(f.read())
    return algorithm.hexdigest()


def file_contrast(file1, file2):
    file1_md5 = hashfile(file1, md5())
    file2_md5 = hashfile(file2, md5())
    return file1_md5 == file2_md5


def main(path, filehash=True):
    ver_dir(path)
    get_all_file()
    all_file = [dir_list, file_list]
    z = ""
    for i in range(2):
        if i == 0:
            pre = "dir:"
        else:
            pre = "file:"
        for x in all_file[i]:
            if i != 0 and filehash == True:
                file_md5 = hashfile(x, md5())
                z = z + pre + x + "\t" + "MD5:" + file_md5 + "\n"
            else:
                z = z + pre + x + "\n"
    with open("ver_allfile.txt", "w") as f:
        f.write(z)



if __name__ == "__main__":
    if argv[1] == "-m" and len(argv) > 2:
        main(argv[2])
    elif argv[1] == "-c" and len(argv) > 3:
        print(file_contrast(argv[2], argv[3]))
    else:
        print(argv[0]+": Parameter error!")
