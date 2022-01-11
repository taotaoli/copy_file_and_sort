import os
import sys
import glob
import re

targetPath = r'D:\shell\bmp'
suffix = r'*.bmp'

dstfile = 'name.txt'

tag_front = 'output_frame_'   # get number from tag_front(.*?)tag_end
tag_end = '_hdr'


def grep_info(tag1, tag2, str_txt):
    pattern_str = '%s(.*?)%s' % (tag1, tag2)
    pattern = re.compile(pattern_str)
    target = int(pattern.findall(str_txt)[0])
    return target


def globname():
    fp = open(dstfile, mode='w')
    fullpath = os.path.join(targetPath+'\\', suffix)
    files = glob.glob(fullpath)
    files.sort(key=lambda x: int(grep_info(tag_front, tag_end, x)))
    for f in files:
        fp.write(f + '\n')

    print('cat full file name to [', dstfile, '] done')
    fp.close()


if __name__ == '__main__':
    if not os.path.exists(targetPath):
        print(targetPath, 'not exist,return !!!')
        sys.exit(0)
    globname()
