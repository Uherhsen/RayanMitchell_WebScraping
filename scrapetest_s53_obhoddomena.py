# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:32:33 2020

Учебник Райан Митчелл Скрапинг Веб-сайтов с помощью Python

Обход отдельного домена
РЕКУРСИВНЫЙ ОБХОД
c 53
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
n = 10 # Условие для окончания цикла
while len(links)>0 and n>0:
    newArticle = links[random.randint(0,(len(links)-1))].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
    n-=1
    