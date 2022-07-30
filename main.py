# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import glob
import threading
from time import sleep

from bs4 import BeautifulSoup
import urllib
import os
import urllib.request
import requests
from datetime import datetime
from pathlib import PurePosixPath

lock = threading.Lock()
success_count = 0
error_count = 0
URL_mp = set()
URL_xing = set()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}


def log(text):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), text)


def run_mp():
    global error_count
    global success_count
    global URL_mp
    global URL_xing
    # set1 = set()
    while True:
        try:
            # 请求网址
            response1 = requests.get("https://iw233.cn/api.php?sort=mp", headers)  # 竖屏壁纸

            # 取得跳转后的网址
            urls_mp = response1.url

            # 取得最后一个分割出来的字符串 即图片名称
            arrUrl_mp = urls_mp.split("/")[-1]

            # 为连接添加%作为分隔号
            urls_mp_2 = urls_mp + "%"

            # 判断网址是否下载过
            if urls_mp in URL_mp:

                log("竖屏重复")

            else:

                data_mp = open("E:/学习/image/竖屏/URL.txt", mode="a+")
                data_mp.write(urls_mp_2)

                fname_mp = "E:\\学习\\image\\竖屏\\" + arrUrl_mp + ".tmp"

                urllib.request.urlretrieve(urls_mp, filename=fname_mp)

                try:
                    os.rename(fname_mp, "E:\\学习\\image\\竖屏\\" + arrUrl_mp)
                    log('竖屏 ' + arrUrl_mp + ' 下载完成')
                    URL_mp.add(urls_mp)
                except:
                    os.remove(fname_mp)
                    URL_mp.add(urls_mp)
                    log("出现错误，删除重复文件" + arrUrl_mp)



        except Exception as r:

            print('未知错误 %s' % r)
            lock.acquire()
            log('报错，直接跳过... *{}'.format(error_count))
            error_count += 1
            lock.release()
            continue


def run_xing():
    global error_count
    global success_count
    global URL_mp
    global URL_xing
    # set1 = set()
    while True:

        try:
            # 请求网址
            response2 = requests.get("https://iw233.cn/api.php?sort=xing", headers=headers)  # 星空

            # 取得跳转后的网址
            urls_xing = response2.url

            # 取得最后一个分割出来的字符串 即图片名称

            arrUrl_xing = urls_xing.split("/")[-1]

            # 为连接添加%作为分隔号
            urls_xing_2 = urls_xing + "%"

            # 判断网址是否下载过
            if urls_xing in URL_xing:

                log("星空重复")

            else:

                data_xing = open("E:/学习/image/星空/URL.txt", mode="a+")
                data_xing.write(urls_xing_2)

                fname_xing = "E:\\学习\\image\\星空\\" + arrUrl_xing + ".tmp"

                urllib.request.urlretrieve(urls_xing, filename=fname_xing)

                try:
                    os.rename(fname_xing, "E:\\学习\\image\\星空\\" + arrUrl_xing)
                    log('星空 ' + arrUrl_xing + ' 下载完成')
                    URL_xing.add(urls_xing)
                except:
                    os.remove(fname_xing)
                    URL_xing.add(urls_xing)
                    log("出现错误，删除重复文件" + arrUrl_xing)



        except Exception as r:

            print('未知错误 %s' % r)
            lock.acquire()
            log('报错，直接跳过... *{}'.format(error_count))
            error_count += 1
            lock.release()
            continue


def delete():
    path = ["E:/学习/image/星空", "E:/学习/image/竖屏"]
    for p in path:
        print(p)
        print("删除前有: ", len(os.listdir(p)), " 个文件...")

        try:
            n = 0
            for infile in glob.glob(os.path.join(p, '*.tmp')):
                os.remove(infile)
                n += 1
            print("删除后: ", len(os.listdir(p)), "删除: ", n, " 个文件""\n\n")
        except Exception as r:
            log("未知错误" + r)
            continue


if __name__ == '__main__':
    data_mp = open("E:/学习/image/竖屏/URL.txt")
    substrings_mp = data_mp.read().split("%")

    data_xing = open("E:/学习/image/星空/URL.txt")
    substrings_xing = data_xing.read().split("%")

    delete()

    for i in range(len(substrings_mp)):
        URL_mp.add(substrings_mp[i])

    for i in range(len(substrings_xing)):
        URL_xing.add(substrings_xing[i])

    for i in range(25):
        threading.Thread(target=run_mp).start()
        log('线程{}启动...'.format(i))
        sleep(0.1)

    for i in range(5):
        threading.Thread(target=run_xing).start()
        log('线程{}启动...'.format(i))
        sleep(0.1)
