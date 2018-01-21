# 2018年1月21日 13点00分
# 作者：cacho
# 爬虫：抓美女套图
# 目标网址：http://www.xingmeng365.com/

from bs4 import BeautifulSoup
import requests
import os
import urllib.request
import sys

num = 1
image_list = []
id = 1

while(id <= 7):
    p = 1
    while(p<=30):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        url = requests.get('http://www.xingmeng365.com/articles.asp?id='+str(id)+'&mm='+str(p), headers=headers)
        # 此处用 “，str(id)” 的话，逗号打印出来会变成 “id=&2”
        print("当前爬取的网址为："+url.url)
        #如果网页设置了charset=gb2312，那么需要设置编码方式为gb2312
        url.encoding = 'gb2312'
        html_doc = url.text
        # 此处用url不带".text"的话报错，Python: object of type 'Response' has no len()
        # 错误解决
        # https://stackoverflow.com/questions/36709165/python-object-of-type-response-has-no-len
        soup = BeautifulSoup(html_doc,"lxml")
        for link in soup.find_all('img'):
            if "/upload/image" in link.get('src'):
                # id=7以后，"../../"改为"/upload"
                image_url = link.get('src')
                # 获得的图片地址有错，需要改成
                 # http://www.xingmeng365.com/upload/image/20170811/20170811203590079007.jpg
                # 即把 “../../” 改为 “http://www.xingmeng365.com/”
                 # id=7 以后为/upload/image/20170811/20170811210596789678.jpg
                 # http://www.xingmeng365.com/upload/image/20170811/20170811210545754575.jpg
                if id <= 6:
                    image_url = "http://www.xingmeng365.com/" + image_url[6:]
                else:  # id=7以后，[6:]改为[1:]
                    image_url = "http://www.xingmeng365.com/" + image_url[1:]
                # 在mian.py当前位置创建图片收集的文件夹Photos
                # 获取标题的内容
                FileName = soup.title.get_text()
                #切换到文件路径，然后创建一个新目录
                os.chdir('D:\BeautifulGirls')
                image_path = 'AllPhoto/' + str(FileName)
                if not os.path.exists(image_path):
                    os.makedirs(image_path)
                #切换到新的目录
                os.chdir(image_path)
                print(image_path)
                print("开始下载第"+str(num)+"张图片："+image_url)
                file = open(str(id)+'.'+str(p)+'-'+str(num)+'.jpg',"wb")
                req = urllib.request.Request(url=image_url, headers=headers)
                try:
                    image = urllib.request.urlopen(req, timeout=20)
                    pic = image.read()
                except Exception as e:
                    print("第"+str(num)+"张图片访问超时，下载失败："+image_url)
                    continue
                file.write(pic)
                print("第"+str(num)+"张图片下载成功")
                #close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作
                file.close()
                num = num + 1
        p = p + 1
    id = id + 1