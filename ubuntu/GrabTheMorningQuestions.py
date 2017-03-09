#coding:utf-8
#抓取http://www.rkpass.cn网上的试题

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
import GrabTheChain
import datetime

cur_dir = '/home/engineman/Desktop/'
folder_name = '软考上午试题'
if os.path.isdir(cur_dir):
    os.mkdir(os.path.join(cur_dir, folder_name))

def getTestPaper(page,url):
    html = urlopen('http://www.rkpass.cn/tk_timu/6_'+page+'_'+url+'_xuanze.html')
    bsObj = BeautifulSoup(html)
    # 找到包含标题的span标签
    titles = bsObj.find_all('span', {'class': 'product-text'})
    # 找到包含试卷内容的span标签
    bsObj = bsObj.find_all('span', {'class': 'shisi_text'})
    # 写入标题
    f.write(titles[1].text + '\n')
    num = 0
    for txt in bsObj:
        num += 1
        txt = txt.text
        txt = re.sub('\s*', '', txt)
        txt = re.sub('.\.', getWord(num), txt)
        if num ==  1:
            f.write(url+'、'+txt)
        elif num == 5:
            f.write(txt+'\n')
        else:
            f.write(txt)

def getWord(num):
    if num == 2:
        return '\n'+'A、'
    elif num == 3:
        return '\n' + 'B、'
    elif num == 4:
        return '\n' + 'C、'
    elif num == 5:
        return '\n' + 'D、'
    else:
        return '\n'


startTime = datetime.datetime.now()

page = -1
while page < len(GrabTheChain.xuanzePage)-1:
    page += 1
    page = str(page)
    num = 0
    f = open('/home/engineman/Desktop/软考上午试题/' + page + '.txt', 'w')
    while num < 75:
        num += 1
        num = str(num)
        getTestPaper(str(GrabTheChain.xuanzePage[int(page)]), num)
        num = int(num)
    f.close()
    page = int(page)
end = datetime.datetime.now()
print(end - startTime)