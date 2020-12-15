# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:36:22 2020

Учебник Райан Митчелл Скрапинг Веб-сайтов с помощью Python
c. 23
"""

from urllib.request import urlopen
html = urlopen("https://www.avito.ru/sankt-peterburg") #"http://pythonscraping.com/pages/page1.html")
print(html.read())
