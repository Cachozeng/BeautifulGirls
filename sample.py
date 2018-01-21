import urllib2

num=1
id=2
while(id <= 10):
    p=1
    while(p<=10):
        url = 'http://www.xingmeng365.com/articles.asp?id='+str(id)+'&mm='+str(p)
        for i in range(1, 10):
            if i<5:
                print("开始下载第" + str(num) + "张图片：" +str(i)+ url)
                print("第" + str(num) + "张图片下载成功"+str(i))
                num=num+1
        p=p+1
    id=id+1



