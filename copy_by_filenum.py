import os
import shutil

targetPath = r'D:\shell\bmp'
suffix = r'.bmp'

dstPath = r'D:\shell\tmp'


def copy_file(src, num):
    srcfile = targetPath + '\\' + src
    dstfile = dstPath + '\\' + str(num) + suffix
    print('copy ', srcfile, 'to ', dstfile)

    shutil.copyfile(srcfile, dstfile)


def rename():
    file = os.listdir(targetPath)
    # file.sort(key=lambda x: int(x.split('_')[1]))  # 以 _ 分割文件名，并以第1个数字排序文件
    for f in file:
        f_lower = f.lower()  # 忽略后缀大小写
        if f_lower.endswith(suffix):
            fileNum = int(f.split('_')[1])  # 以 _ 分割文件名，并或第1个数字
            # print(f)
            copy_file(f, fileNum)


if __name__ == '__main__':
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)
    rename()
