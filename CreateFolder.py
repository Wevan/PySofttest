#coding:utf-8
# 创建文件夹
import os

cur_dir = '/home/engineman/Desktop'
folder_name = 'baiduzhidao'
if os.path.isdir(cur_dir):
    os.mkdir(os.path.join(cur_dir, folder_name))