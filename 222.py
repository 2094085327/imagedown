import os
import hashlib


def get_md5(file):
    file = open(file, 'rb')
    md5 = hashlib.md5(file.read())
    file.close()
    md5_values = md5.hexdigest()
    return md5_values


def delete():
    file_path = "E:/学习/image/竖屏"
    os.chdir(file_path)
    file_list = os.listdir(file_path)
    md5_list = []
    for file in file_list:
        md5 = get_md5(file)
        if md5 not in md5_list:
            md5_list.append(md5)
        else:
            print(md5)
            os.remove(file)


def filecount():
    # 获取目录下（不包含子目录）的文件数
    # file_nums = sum([os.path.isdir(listx) for listx in os.listdir("E:\学习\image\竖屏")])

    # 获取目录下（包含子目录）的所有文件数
    file_nums = sum([len(files) for root, dirs, files in os.walk("E:/学习/image/竖屏")])

    return file_nums


if __name__ == '__main__':
    oldf = filecount()

    print('去重前有', oldf, '个文件\n\n请稍等正在删除重复文件...')

    delete()

    print('\n\n去重后剩', filecount(), '个文件')

    print('\n\n一共删除了', oldf - filecount(), '个文件\n\n')
