import os
import sys

targetPath = r'D:\work\python\copy_bmp_by_filenum\raw'
suffix = r'.raw'

dstfile = 'name.txt'


def catname():
    fp = open(dstfile,mode='w')
    file = os.listdir(targetPath)
    file.sort(key=lambda x: int((x[:-4].split('_')[-1])[2:]))  # cut suffix, 以 _ 分割文件名，取最后一个str，并cut前两个字符, aa_bb_cc_dd_ee0.bmp
    for f in file:
        f_lower = f.lower()  # 忽略后缀大小写
        if f_lower.endswith(suffix):
            fullpath = targetPath + '\\' + f + '\n'
            fp.write(fullpath)

    print('cat full file name to [', dstfile, '] done')
    fp.close()


if __name__ == '__main__':
    if not os.path.exists(targetPath):
        print(targetPath, 'not exist,return !!!')
        sys.exit(0)
    catname()

