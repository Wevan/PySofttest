#coding:utf-8
#抓取http://www.rkpass.cn网上的试题
#软考中级，软件设计师下午试题
from urllib.request import urlretrieve
from urllib.request import urlopen

import re
from bs4 import BeautifulSoup
import os
import GrabTheChain

#创建文件夹
cur_dir = 'D:/PyCrawler/PySofttest/problems'
folder_name = '\u8f6f\u8003\u4e0b\u5348\u8bd5\u9898'
if os.path.isdir(cur_dir):
    os.mkdir(os.path.join(cur_dir, folder_name))

#抓取试卷内容
def getTestPaper(page,url):

    f = open('D:/PyCrawler/PySofttest/problems/\u8f6f\u8003\u4e0b\u5348\u8bd5\u9898/'+ page +'/'+folder_name + '/' + url + '.txt', 'w', encoding='utf-8')
    html = urlopen('http://www.rkpass.cn/tk_timu/6_'+page+'_'+url+'_anli.html')
    bsObj = BeautifulSoup(html,"lxml")

    #找到试卷图片的url
    pictures = bsObj.findAll('img',{'src':re.compile('http\:\/\/www\.rkpass\.cn\:8080\/.*\/.*\/.*\/.*\.(png|jpg)')})
    #找到包含标题的span标签W
    titles = bsObj.find_all('span',{'class':'product-text'})
    #找到包含试卷内容的span标签
    bsObj = bsObj.find_all('span', {'class': 'shisi_text'})
    # #写入标题
    # f.write(titles[1].text+'\n')
    #设定记录数
    num = 0
    for txt in bsObj:
        #纪录数自增
        num += 1
        txt = txt.text
        if num > 1:
            #去除所有的空格
            txt = re.sub('\s*','',txt)
            #匹配到 问题： 这种格式后，将该位置转换成  换行+问题：
            txt = re.sub('..\uff1a','\n\u95ee\u9898\uff1a',txt)
            # 匹配到 分） 这种格式后，将该位置转换成  分）+换行
            txt = re.sub('\u5206\）','\u5206\uff09\n',txt)
        f.write(txt)
    for picture in pictures:
        url = re.compile('http\:\/\/www\.rkpass\.cn\:8080\/ruankao\_work\_version\_0103\/userfile\/image\/(.*)')
        res = url.search(picture['src']).groups()
        print(res)
        urlretrieve(picture['src'],'D:/PyCrawler/PySofttest/problems/\u8f6f\u8003\u4e0b\u5348\u8bd5\u9898/'+page+'/' + folder_name +'/'+str(res[0]))
    f.close()


page = -1
while page < len(GrabTheChain.xuanzePage)-1:
    page += 1
    page = str(page)
    num = 0
    cur_dir = 'D:/PyCrawler/PySofttest/problems/\u8f6f\u8003\u4e0b\u5348\u8bd5\u9898/'
    folder_name = str(GrabTheChain.anliPage[int(page)])
    if os.path.isdir(cur_dir):
        os.mkdir(os.path.join(cur_dir, folder_name))
    while num < 6:
        num += 1
        num = str(num)
        cur_dir = 'D:/PyCrawler/PySofttest/problems/\u8f6f\u8003\u4e0b\u5348\u8bd5\u9898/' + str(GrabTheChain.anliPage[int(page)]) + '/'
        folder_name = num
        if os.path.isdir(cur_dir):
            os.mkdir(os.path.join(cur_dir, folder_name))
        getTestPaper(str(GrabTheChain.anliPage[int(page)]), num)
        num = int(num)
    page = int(page)

