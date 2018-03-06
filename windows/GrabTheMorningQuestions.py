#encoding:utf-8
#抓取http://www.rkpass.cn网上的试题
#软考终极，软件设计师，上午的试题

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
import GrabTheChain
import datetime
cur_dir = 'D:/PyCrawler/PySofttest/problems'
folder_name = '\u8f6f\u8003\u4e0a\u5348\u8bd5\u9898'
if os.path.isdir(cur_dir):
    os.mkdir(os.path.join(cur_dir, folder_name))

def getTestPaper(page,url):
    html = urlopen('http://www.rkpass.cn/tk_timu/6_'+page+'_'+url+'_xuanze.html')
    bsObj = BeautifulSoup(html,"lxml")
    # 找到包含标题的span标签
    titles = bsObj.find_all('span', {'class': 'product-text'})
    bsObj = bsObj.find_all('span', {'class': 'shisi_text'})
    if int(url) < 2:
        # 写入标题
        f.write(titles[1].text + '\n')
    num = 0
    for txt in bsObj:
        num += 1
        txt = txt.text
        txt = re.sub('\s*', '', txt)
        txt = re.sub('.\.', getWord(num), txt)
        if num ==  1:
            f.write(url+'\u3001'+txt)
        elif num == 5:
            f.write(txt+'\n')
        else:
            f.write(txt)

def getWord(num):
    if num == 2:
        return '\n'+'A\u3001'
    elif num == 3:
        return '\n' + 'B\u3001'
    elif num == 4:
        return '\n' + 'C\u3001'
    elif num == 5:
        return '\n' + 'D\u3001'
    else:
        return '\n'

page = -1
while page < len(GrabTheChain.xuanzePage)-1:
    page += 1
    page = str(page)
    num = 0
    f = open('D:/PyCrawler/PySofttest/problems/\u8f6f\u8003\u4e0a\u5348\u8bd5\u9898/' + str(GrabTheChain.xuanzePage[int(page)]) + '.txt', 'w',encoding='utf-8')
    while num < 75:
        num += 1
        num = str(num)
        getTestPaper(str(GrabTheChain.xuanzePage[int(page)]),num)
        num = int(num)
    f.close()
    page = int(page)