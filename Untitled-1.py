# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
def getHtml(url):
    req = requests.get(url)
    req.encoding = "gbk"
    return req.content
def getcityhtml(html):
    reg = r'<a  href=(.*?) >(.*?)</a>'.encode("gbk")
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    return imglist
def getalltig(cityhtml):
    reg = r'<div class="pt4 floatl">(.*?)</div>'.encode("gbk")
    imgre = re.compile(reg)
    imglist = imgre.findall(cityhtml)
    for imgurl in imglist:
        # print(imgurl.decode('gbk'))
        findtig(imgurl.decode('gbk'))
    return imglist


def findnexthtml(html):
    reg = r'href="(.*?)">下一页'.encode("gbk")
    imgre = re.compile(reg)
    nextimglist = imgre.findall(html)
    return nextimglist


def findtig(html):
    reg = r'<span class=".*?note">(.*?)</span>'
    imgre = re.compile(reg)
    nextbaozhengjins = imgre.findall(html)
    print("")
    for nextbaozhengjin in nextbaozhengjins:
        print(nextbaozhengjin, end='#')
    print()
    return nextbaozhengjins


def findmostdata(html):
    reg = r'<a href=(.*?) target="_blank" title=.*?>'.encode("gbk")
    imgre = re.compile(reg)
    nextfenshus = imgre.findall(html)
    return nextfenshus


def findloupanmingcheng(html):
    # reg = r'<span class="gray6">写字楼名称：</span>\n(.*?)\n'.encode("gbk")
    # imgre = re.compile(reg)
    # nextfuwushus = imgre.findall(html)
    # for nextfuwushu in nextfuwushus:
    #     print("楼盘名称："+nextfuwushu.decode('gbk'))
    soup = BeautifulSoup(html, "html.parser",from_encoding="GBK")
    divPager = soup.find_all('dt')
    for div in divPager:
        print(div.get_text())
def findloupandizhi(html):
    reg = r'楼盘地址：</span>(.*?)</dt>'.encode("gbk")
    imgre = re.compile(reg)
    nextjines = imgre.findall(html)
    for nextjine in nextjines:
        print("楼盘地址：" + nextjine.decode('gbk'))
    return nextjines


# 找到員工人數
def finddengji(html):
    reg = r'</span>级：(.*?)</span></dd>'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("等级：" + nextrensu.decode('gbk'))
    return nextrensus


def findjianzhumianji(html):
    reg = r'建筑面积：<span class="black ">(.*?)</span></dd>'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("建筑面积：" + nextrensu.decode('gbk'))
    return nextrensus


def findzongcengshu(html):
    reg = r'所在楼层：</span>(.*?)</dd>'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("总层数：" + nextrensu.decode('gbk'))
    return nextrensus


def findbiaozhuncengmianji(html):
    reg = r'标准层面积：</span>(.*?)</dd>'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("标准层面积：" + nextrensu.decode('gbk'))
    return nextrensus


def findkaifashang(html):
    reg = r'开 发 商：</span>(.*?)</dd>'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("开发商：" + nextrensu.decode('gbk'))
    return nextrensus


def findjungongshijian(html):
    reg = r'<span class="gray6">竣工时间：</span>(.*?)\n'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("竣工时间：" + nextrensu.decode('gbk'))
    return nextrensus


def findwuyegongsi(html):
    reg = r'<span class="gray6">物业公司：</span>(.*?)</dd>'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("物业公司：" + nextrensu.decode('gbk'))
    return nextrensus


def findzujin(html):
    reg = r'>(.*?)</span></span><span class="black">\s*[\s\S]*?\s*元/平米·天</span>'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("租金：" + nextrensu.decode('gbk'))
    return nextrensus


def findzhuangxiu(html):
    reg = r'<span class="gray6">装<span class="padl27"></span>修：</span>(.*?)\n'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("装修：" + nextrensu.decode('gbk'))
    return nextrensus


def findzhongjiexingming(html):
    reg = r'<span id="agentname">(.*?)</span>'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("中介姓名：" + nextrensu.decode('gbk'))
    return nextrensus


def findzhongjiedianhua(html):
    reg = r'<label id="mobilecode">(.*?)</label>'.encode("gbk")
    imgre = re.compile(reg)
    nextrensus = imgre.findall(html)
    for nextrensu in nextrensus:
        print("中介电话：" + nextrensu.decode('gbk'))
    return nextrensus


mostdatahtml = "http://office.fang.com/zu/1_60594107.html"
mostdatahtml = getHtml(mostdatahtml)
# 楼盘名称
findloupanmingcheng(mostdatahtml)
# 楼盘地址
findloupandizhi(mostdatahtml)
# 等级
finddengji(mostdatahtml)
# 建筑面积
findjianzhumianji(mostdatahtml)
# 总层数
findzongcengshu(mostdatahtml)
# 标准层面积
findbiaozhuncengmianji(mostdatahtml)
# 开发商
findkaifashang(mostdatahtml)
# 竣工时间
findjungongshijian(mostdatahtml)
# 物业公司
findwuyegongsi(mostdatahtml)
# 租金
findzujin(mostdatahtml)
# 装修
findzhuangxiu(mostdatahtml)
# 中介姓名
findzhongjiexingming(mostdatahtml)
# 中介电话
findzhongjiedianhua(mostdatahtml)

