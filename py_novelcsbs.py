#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
# import urllib3
# from urllib3.request import urlretrieve
import requests
# regex = re.compile(r'(MyGame\:getAppConfig\(\):getImgName\(\"([#."a-zA-Z1-9_]+)\"\))')
# regex = re.compile(r'eval(.*)\$', re.DOTALL)
import shutil

from lxml import etree
from xml.etree import ElementTree

import lxml.html.soupparser as soupparser



# import sys
# from reportlab.lib.pagesizes import portrait
# from reportlab.pdfgen import canvas
# from PIL import Image

base_url = "https://www.biquyun.com/0_773/"

page_list = ["/list/"]

chapter_next_list = []

def main():

    book_item("https://www.biquyun.com/0_773/")
    # chapter_item("http://www.yqhy.org/read/1/1390/23997879.html", "100")

def list_item(pageurl):
    # html = etree.HTML(url)
    page_list.append(pageurl)
    html = etree.parse("{0}{1}".format(base_url, pageurl), etree.HTMLParser())
    html_data = etree.tostring(html, pretty_print=True)
    res = html_data.decode('utf-8')
    # print(res)

    pic_items = html.xpath('/html/body/div/div/div/div/article/div/ul/li/a/@href')
    # print(pic_items)
    for pic_item in pic_items:
        print(pic_item)
        pic_url = pic_item.encode('utf-8').decode()
        book_item(pic_url)

    print("-------------->")
    pages = html.xpath('/html/body/div/div/div/a/@href')
    # print(pages)
    for book in pages:
        book_url = book.encode('utf-8').decode()
        include = False
        for page in page_list:
            if book_url == page:
                include = True
        if include == False:
            print(book_url)
            list_item(book_url)
        # print(book_url)
        # if book_url != pageurl :
        #     print(book_url)
        #     list_item(book_url)


def book_item(bookurl):
    res = requests.get(bookurl, verify=False)
    # res.encoding="gbk"
    res.encoding = "gbk"
    # res.content.decode('gbk').encode('utf-8')
    html_data = ""
    if res.status_code == requests.codes.ok:
        # print(res.text)
        # html_data = res.text
        # print(res.content)
        html_data = res.content

    # regex = re.compile(r'(\d+)', re.DOTALL)
    # mo = regex.search(bookurl)
    # bookdir = ""
    # if None != mo:
    #     print(mo.group(1))
    #     bookdir = os.path.join(os.getcwd(), mo.group(1))
    #     if not os.path.exists(bookdir):
    #         os.makedirs(bookdir)


    # html = etree.parse(bookurl, etree.HTMLParser())
    # html_data = etree.tostring(html, pretty_print=True)
    # res = html_data.decode('utf-8')
    # print(res)
    demo = soupparser.fromstring(res.content)
    t = etree.tostring(demo, encoding="utf-8", pretty_print=True)
    # print(t.decode("utf-8"))
    html = etree.HTML(t.decode("utf-8"))

    # book = html.xpath('/html/body/div/div/div/h1')
    # print(book)
    # chapter_list = html.xpath('/html/body/div/div/div/h1')
    # for book_name in book:
    #     print(book_name.text)
    book_name = "长生不死"
    bookdir = os.path.join(os.getcwd(), book_name)
    if not os.path.exists(bookdir):
        os.makedirs(bookdir)

    book_file_path = os.path.join(os.getcwd(), book_name, "{0}.txt".format(book_name))
    if os.path.exists(book_file_path):
        os.remove(book_file_path)
        # f = open(book_file, 'w')
        # print(outfile)
        # f.close()
    # print(outfile + " created.")

    book_file = open(book_file_path, "w+")

    # chapter_list = html.xpath('/html/body/div/div/dl/dd/a/@href')
    div_list = html.xpath('//div[@id="list"]')
    print(div_list[0])
    chapter_list = div_list[0].xpath('//dl/dd/a/@href')
    print(chapter_list)
    for chapter in chapter_list:
        chapterl_url = base_url + chapter.encode('utf-8').decode().replace('\n', '')
        print(chapterl_url)
        # chapterl_url = chapterl_url.replace('\n','')
        # print(chapterl_url)
        chapter_item(chapterl_url, book_file)
    #     chapterl_url = chapter.encode('utf-8').decode()
    #     print(chapterl_url)
        # chapter_item(chapterl_url, bookdir)

    book_file.close()

def chapter_item(chapterl_url, book_file):
    # if not os.path.exists(bookdir):
    #     os.makedirs(bookdir)
    chapter_next_list.append(chapterl_url)
    res = requests.get(chapterl_url, verify=False)
    res.encoding = "gbk"
    html_data = ""
    if res.status_code == requests.codes.ok:
        # print(res.text)
        # html_data = res.text
        html_data = res.content
    demo = soupparser.fromstring(html_data)
    t = etree.tostring(demo, encoding="utf-8", pretty_print=True)
    # print(t.decode("utf-8"))
    html = etree.HTML(t.decode("utf-8"))
    # html = etree.HTML(html_data)
    # html = etree.parse("{0}{1}".format(base_url, chapterl_url), etree.HTMLParser())
    # html_data = etree.tostring(html, pretty_print=True)
    # res = html_data.decode('utf-8')
    # print(res)

    body_list = html.xpath('//div[@id="content"]')
    print(body_list)
    for body in body_list[0]:
        print(body)
        # img_url = body.encode('utf-8').decode()
        print(body.text_content())
        
        # body = ElementTree.tostring(body, 'utf-8')
        # body_temp = body.split()

        # body = ""
        # for tmp in body_temp:
        #     body = body + tmp.strip()
        # body = body.replace('<p>','').replace('</p>', '').replace('<br/><br/>', '\n')
        # book_file.write(body + '\n')

if __name__ == '__main__':
    main()
