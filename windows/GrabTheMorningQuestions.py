#encoding:utf-8
#抓取http://www.rkpass.cn网上的试题
#软考终极，软件设计师，上午的试题

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
import GrabTheChain
import datetime
cur_dir = 'C:/Users/Administrator/Desktop'
folder_name = '\u8f6f\u8003\u4e0a\u5348\u8bd5\u9898'
if os.path.isdir(cur_dir):
    os.mkdir(os.path.join(cur_dir, folder_name))

def getTestPaper(page,url):
    html = urlopen('http://www.rkpass.cn/tk_timu/6_'+page+'_'+url+'_xuanze.html')
    bsObj = BeautifulSoup(html)
    bsObj = bsObj.find_all('span', {'class': 'shisi_text'})
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
while page < len(c.xuanzePage)-1:
    page += 1
    page = str(page)
    num = 0
    f = open('C:/Users/Administrator/Desktop/\u8f6f\u8003\u4e0a\u5348\u8bd5\u9898/' + str(GrabTheChain.xuanzePage[int(page)]) + '.txt', 'w',encoding='utf-8')
    while num < 75:
        num += 1
        num = str(num)
        getTestPaper(str(GrabTheChain.xuanzePage[int(page)]),num)
        num = int(num)
    f.close()
    page = int(page)
