@echo off

d:
cd D:\BeautifulGirls

git init
git remote add gitee https://gitee.com/Cacho/BeautifulGirls.git
git remote add github https://github.com/Cachozeng/D:\BeautifulGirls.git

git pull gitee master
git pull github master

git add .
git commit -m "add BeautifulGirls"
git push -f gitee master
git push github master

pause