# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:03:14 2020

Учебник Райан Митчелл Скрапинг Веб-сайтов с помощью Python
c. 30
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
        
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features = "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("https://www.avito.ru/sankt-peterburg") #("http://pythonscraping.com/pages/page1.html")# https://www.avito.ru/sankt-peterburg")
if title == None:
    print("Title not be found")
else:
    print(title)