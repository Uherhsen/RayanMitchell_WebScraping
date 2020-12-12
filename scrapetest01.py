# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:24:24 2020

Учебник Райан Митчелл Скрапинг Веб-сайтов с помощью Python
c. 27
"""
from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
bs0bj = BeautifulSoup(html.read(),features = "html.parser")
print(bs0bj.h1)
