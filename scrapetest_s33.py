# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:03:30 2020
Учебник Райан Митчелл Скрапинг Веб-сайтов с помощью Python
Пример со страницы 31:
bsObj.findAll("table")[4].findAll("tr")[2].find("td").findAll("div")[1].find("a")

c. 34
findAll(tag, attributes, recursive, limit, keywords)
find(tag, attributes, recursive, keywords)

bsObj.tagname.tagname2 (например bsObj.body.h1)
bsObj.find
bsObj.findAll("span",{"class":"green"}) (поиск по атрибутам)
bsObj.findAll(text = "the Text") (ищет текст)
аргумент recusive = False/True (потомки/теги верхнего уровня, с 35)
id = text (keyword)
bs0Obj.findAll(id="text") == bs0Obj.findAll("",{"id":"text"})

bs0Obj.findAll(class_="green") == bs0Obj.findAll("",{"class":"green"})

name.get_text()

еще объекты для поиска:
    BeautifulSoup
    Tag - получают списками или индивидуально путем вызова find и findAll для объекта BeautifulSoup
    NavigableString - исп-ся для представления текста внутри тегов
    Comment - исп-ся для поиска комментариев
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features="html.parser")
nameList = bsObj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())