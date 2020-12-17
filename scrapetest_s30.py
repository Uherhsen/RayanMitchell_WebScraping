# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:03:14 2020

Учебник Райан Митчелл Скрапинг Веб-сайтов с помощью Python
c. 30
 bsObj.tagname первое вхождение тега
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
        
    except HTTPError as e:
        print("HTML код не получен")
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features = "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%80%D0%B0%D0%B1%D0%BB%D1%8C_%D0%A2%D0%B5%D1%81%D0%B5%D1%8F") #("http://pythonscraping.com/pages/page1.html")# https://www.avito.ru/sankt-peterburg")
if title == None:
    print("Title not be found")
else:
    print(title)