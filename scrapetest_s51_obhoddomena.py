# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:32:33 2020

Учебник Райан Митчелл Скрапинг Веб-сайтов с помощью Python

Обход отдельного домена
c 51
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)

# Получение всех ссылок с вики:
#for link in bsObj.findAll("a"):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])

# Получение только ссылок на статьи вики

# они располагаются внутри блоков div c id ="bodycontent"
# URl-адреса не содержат точек с запятой
# URl-адреса ачинаются с /wiki/

# Используя эти правила получим код:

for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
        

