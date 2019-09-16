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

# import sys
# from reportlab.lib.pagesizes import portrait
# from reportlab.pdfgen import canvas
# from PIL import Image

base_url = "http://www.yqhy.org"

page_list = ["/list/"]

chapter_next_list = []

def main():

    book_item("http://www.yqhy.org/read/1/1390/")
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
    res = requests.get(bookurl)
    html_data = ""
    if res.status_code == requests.codes.ok:
        # print(res.text)
        html_data = res.text
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
    html = etree.HTML(html_data)

    book = html.xpath('/html/body/div/div/div/h1')
    print(book)
    # chapter_list = html.xpath('/html/body/div/div/ul/li/a/@href')
    for book_name in book:
        print(book_name.text)
        bookdir = os.path.join(os.getcwd(), book_name.text)
        if not os.path.exists(bookdir):
            os.makedirs(bookdir)

    book_file_path = os.path.join(os.getcwd(), book_name.text, "{0}.txt".format(book_name.text))
    if os.path.exists(book_file_path):
        os.remove(book_file_path)
        # f = open(book_file, 'w')
        # print(outfile)
        # f.close()
    # print(outfile + " created.")

    book_file = open(book_file_path, "w+")

    chapter_list = html.xpath('/html/body/div/div/dl/dd/a/@href')
    for chapter in chapter_list:
        # print(chapter)
        chapterl_url = chapter.encode('utf-8').decode().replace('\n', '')
        # chapterl_url = chapterl_url.replace('\n','')
        # print(chapterl_url)
        chapter_item(chapterl_url, book_file)
    #     chapterl_url = chapter.encode('utf-8').decode()
    #     print(chapterl_url)
    #     chapter_item(chapterl_url, bookdir)

    book_file.close()

def chapter_item(chapterl_url, book_file):
    # if not os.path.exists(bookdir):
    #     os.makedirs(bookdir)
    chapter_next_list.append(chapterl_url)
    res = requests.get(chapterl_url)
    html_data = ""
    if res.status_code == requests.codes.ok:
        # print(res.text)
        html_data = res.text

    html = etree.HTML(html_data)
    # html = etree.parse("{0}{1}".format(base_url, chapterl_url), etree.HTMLParser())
    # html_data = etree.tostring(html, pretty_print=True)
    # res = html_data.decode('utf-8')
    # print(res)

    body_list = html.xpath('/html/body/div/table/tbody/tr/td/div/table/tbody/tr/td/div/p')
    for body in body_list:
        # print(chapter)
        # img_url = body.encode('utf-8').decode()
        # print(body)
        print(body.text)
        # print(body.tag)
        # print(inner_xml(body))
        body = ElementTree.tostring(body, 'unicode')#.replace('<p>','').replace('</p>', '').replace('\t', '').replace('\n','').replace('\r', '').replace('<br /><br />', '\n')
        body_temp = body.split() # tmp_str = ['a' ,'b' ,'c']

        body = ""
        for tmp in body_temp:
            body = body + tmp.strip()
        body = body.replace('<p>','').replace('</p>', '').replace('<br/><br/>', '\n')
        book_file.write(body + '\n')

if __name__ == '__main__':
    main()
