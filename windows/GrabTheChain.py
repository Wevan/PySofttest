#coding:utf-8
#获取页面上的所有链接
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime

#获取页面内所有下午试题链接的列表
def getAnliLinks(includeUrl):
    html = urlopen(includeUrl)
    bsObj = BeautifulSoup(html,"lxml")
    anliLinks = bsObj.find_all('a',{'href':re.compile('tk\_paper\/.*anli\.html')})
    anliLink = []
    for link in anliLinks:
        link = link['href']
        link = re.findall('tk\_paper\/6\_(.+?)\_anli\.html',link)
        anliLink.append(link[0])
    return anliLink

#获取页面内所有上午试题链接的列表
def getXuanzeLinks(includeUrl):
    html = urlopen(includeUrl)
    bsObj = BeautifulSoup(html)
    xuanzeLinks = bsObj.find_all('a', {'href': re.compile('tk\_paper\/.*xuanze\.html')})
    xuanzeLink = []
    for link in xuanzeLinks:
        link = link['href']
        link = re.findall('tk\_paper\/6\_(.+?)\_xuanze\.html', link)
        xuanzeLink.append(link[0])
    return xuanzeLink

num = -1
anliPage = []
xuanzePage = []
while num < 3 :
    num += 1
    num = str(num)
    anliPage.extend(getAnliLinks('http://www.rkpass.cn/tk_index.jsp?CurrentPage=' + num + '&year=&px_type=0&kemu_id=6'))
    xuanzePage.extend(getXuanzeLinks('http://www.rkpass.cn/tk_index.jsp?CurrentPage=' + num + '&year=&px_type=0&kemu_id=6'))
    num = int(num)
print(len(xuanzePage))
