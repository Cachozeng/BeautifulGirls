# 2018年1月21日 13点00分
# 作者：cacho_37967865
# 爬虫：抓美女套图
# 目标网址：http://www.xingmeng365.com/

from bs4 import BeautifulSoup
import requests
import os
import urllib.request

num = 1
id = 1

#目前网站id最大为759
while(id <= 759):
    p = 1
    while(p<=2):
        #headers设置爬虫
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        #通过参数id控制美女，参数p控制第几页
        url = requests.get('http://www.xingmeng365.com/articles.asp?id='+str(id)+'&mm='+str(p), headers=headers)
        print("当前爬取的网址为："+url.url)
        #如果网页设置了charset=gb2312，那么需要设置编码方式为gb2312，否则乱码
        url.encoding = 'gb2312'
        html_doc = url.text
        # 此处用url不带".text"的话报错，Python: object of type 'Response' has no len()
        # 错误解决：https://stackoverflow.com/questions/36709165/python-object-of-type-response-has-no-len
        soup = BeautifulSoup(html_doc,"lxml")
        for link in soup.find_all('img'):
            #通过图片路径我们发现每页只有一张图片满足要求，/upload/image可以筛选出我们要的图片
            if "/upload/image" in link.get('src'):
                image_url = link.get('src')
                #  id=7以前，图片的路径是../../upload/image/20170811/20170811203590079007.jpg
                 # id=7 以后为/upload/image/20170811/20170811210596789678.jpg
                if id <= 6:
                    image_url = "http://www.xingmeng365.com/" + image_url[6:]
                else:
                    image_url = "http://www.xingmeng365.com/" + image_url[1:]   # id=7以后，[6:]改为[1:]
                #获取h1标题
                FileName = soup.find('h1').get_text()
                # 获取标题的内容
               # FileName = soup.title.get_text()
                #切换到文件相对路径，在此路径创建一个新目录
                #os.chdir('D:\BeautifulGirls')
                #放到其他路径
                os.chdir('F:\Lingwei')
                image_path = 'AllPhoto/' + str(FileName)
                if not os.path.exists(image_path):
                    os.makedirs(image_path)
                #切换到新的目录，图片才能存入到新创建的目录下
                os.chdir(image_path)
                print("开始下载第"+str(num)+"张图片："+image_url)
                #可以自定义命名图片名称，好检索
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