@echo off

d:
cd D:\BeautifulGirls

git init
git remote add gitee https://gitee.com/Cacho/BeautifulGirls.git
git remote add github https://github.com/Cachozeng/BeautifulGirls.git

git add .
git commit -m "add BeautifulGirls"
git push -f gitee master
git push -f github master

pause