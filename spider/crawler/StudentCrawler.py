# -*- coding: utf-8 -*-
__author__ = 'zhuqi259'

"""
抓取gim数据
"""

import urllib.request
from bs4 import BeautifulSoup
import logging
import codecs
import time
from multiprocessing.dummy import Pool as ThreadPool

__base__ = "http://gim.jlu.edu.cn"
__storage__ = "D:\\student"
__storage_file__ = "D:\\gim.csv"

# 借助logging多线程写入文件
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(__storage_file__, 'a', 'utf-8')  # csv utf-8 乱码 => utf-8 有BOM头, 故使用 filemode = 'a'
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
root_logger.addHandler(handler)

__prefix__ = "http://gim.jlu.edu.cn/glc/glc_sanzhu_print.jsp?menu=shenpibiao&stuno="
__begin__, __end__ = 2009, 2016
__nos__ = ["11", "12", "13", "14", "15",
           "21", "22", "23", "24", "25",
           "31", "32", "33", "34",
           "41", "42", "43", "44", "45",
           "51", "52", "53", "54", "55",
           "61", "62", "63", "64", "65",
           "71", "72", "73", "74", "75", "76", "77", "78",
           "81", "82",
           "91", "92", "93", "95", "96"]

__urls__ = []


class Student:
    def __init__(self):
        self.id = ''  # 学号
        self.username = ''
        self.gender = 0
        self.department = ''
        self.major = ''
        self.teacher = ''
        self.telephone = ''
        self.email = ''

    def __str__(self):
        return "Student : { id=%s, username=%s, gender=%d, department=%s, \
major=%s, teacher=%s, telephone=%s,email=%s }" % (
            self.id, self.username, self.gender, self.department, self.major, self.teacher, self.telephone, self.email)

    def str_2_csv(self):
        return "%s,%s,%d,%s,%s,%s,%s,%s" % (
            self.id, self.username, self.gender, self.department, self.major, self.teacher, self.telephone, self.email)


def url_open(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    return response.read()


def save_img(pic_url):
    # TODO 保存图片
    pass


def parse(url):
    time.sleep(0.1)
    html_doc = url_open(url).decode('gbk')
    soup = BeautifulSoup(html_doc, 'html.parser')
    mytable = soup.find('table', class_='mytable')
    if mytable:
        s = Student()
        pic = mytable.find('img')
        pic_url = __base__ + pic.get('src')
        save_img(pic_url)  # 保存图片
        trs = mytable.find_all('tr')
        tds = trs[0].find_all('td')
        s.id = tds[1].string
        s.username = tds[3].string
        s.gender = 0 if tds[5].string == u'男' else 1
        tds = trs[1].find_all('td')
        s.department = tds[1].string
        s.major = tds[3].string
        s.teacher = tds[5].string
        tds = trs[4].find_all('td')
        s.telephone = tds[3].string
        tds = trs[5].find_all('td')
        s.email = tds[3].string

        logging.info(s.str_2_csv())
        # print(s)
    else:
        print("-")


def batchCrawler(prefix, begin, end):
    for i in range(begin, end + 1):
        url = prefix + str(i)
        parse(url)


def add_2_urls(prefix, begin, end):
    for i in range(begin, end + 1):
        url = prefix + str(i)
        __urls__.append(url)


def doSomething():
    # csv utf-8 乱码
    with open(__storage_file__, 'wb') as f:
        f.write(codecs.BOM_UTF8)
    logging.info(u"学号,姓名,性别(0男1女),院系,专业,导师,手机,邮箱")
    for i in range(__begin__, __end__ + 1):
        head = str(i)
        for no in __nos__:
            batchCrawler(__prefix__ + head + no, 1001, 1300)
            batchCrawler(__prefix__ + head + no, 2001, 2300)
            batchCrawler(__prefix__ + head + no, 4001, 4300)


def doSomethingByThread():
    # csv utf-8 乱码
    with open(__storage_file__, 'wb') as f:
        f.write(codecs.BOM_UTF8)
    logging.info(u"学号,姓名,性别(0男1女),院系,专业,导师,手机,邮箱")
    for i in range(__begin__, __end__ + 1):
        head = str(i)
        for no in __nos__:
            add_2_urls(__prefix__ + head + no, 1001, 1300)
            add_2_urls(__prefix__ + head + no, 2001, 2300)
            add_2_urls(__prefix__ + head + no, 4001, 4300)

    # Make the Pool of workers
    pool = ThreadPool(10)
    # Open the urls in their own threads and return the results
    # results = pool.map(parse, __urls__)
    pool.map(parse, __urls__)
    # close the pool and wait for the work to finish
    pool.close()
    pool.join()


if __name__ == '__main__':
    doSomethingByThread()
