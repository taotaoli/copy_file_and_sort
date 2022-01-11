import os
import sys
import glob
import re

targetPath = r'D:\shell\bmp'
suffix = '*.bmp'

dstfile = 'name.txt'

tag_front = 'output20bit_'   # get number from tag_front(.*?)tag_end
tag_end = '_final'


def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False


def grep_info(tag1, tag2, str_txt):
    pattern_str = '%s(.*?)%s' % (tag1, tag2)
    pattern = re.compile(pattern_str)
    target_str = pattern.findall(str_txt)[0]
    if is_number(target_str):
        return int(target_str)
    else:
        print('grep [', target_str, '] is not a number ,return !!!')
        sys.exit(0)


def globname():
    fp = open(dstfile, mode='w')
    fullpath = os.path.join(targetPath+'\\', suffix)
    files = glob.glob(fullpath)
    if len(files) == 0:
        print('no ', suffix, 'found , return !!!')
        return
    files.sort(key=lambda x: int(grep_info(tag_front, tag_end, x)))
    for f in files:
        print(f)
        fp.write(f + '\n')

    print('cat full file name to [', dstfile, '] done')
    fp.close()


if __name__ == '__main__':
    if not os.path.exists(targetPath):
        print(targetPath, 'not exist,return !!!')
        sys.exit(0)
    globname()
