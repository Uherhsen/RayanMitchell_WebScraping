# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:03:30 2020
Учебник Райан Митчелл Скрапинг Веб-сайтов с помощью Python
c. 34
bsObj.tagname.tagname2 (например bsObj.body.h1)
bsObj.find
bsObj.findAll("span",{"class":"green"})
name.get_text()
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features="html.parser")
nameList = bsObj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())