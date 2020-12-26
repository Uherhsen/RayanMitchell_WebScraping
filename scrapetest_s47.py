# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:35:46 2020

Учебник Райан Митчелл Скрапинг Веб-сайтов с помощью Python

Регулярные выражения с 47 работа с атрибутами 
для обучения используется:
    http://bit.ly/1KGe2Qk оно же (http://www.pythonscraping.com/pages/page3.html)
    
Получить доступ к питоновскому списку атрибутов можно ввтоматически , вызвав 
myTag.attrs
Например адрес файла изображения можно найти с помощью следующей строки 
myTag.attrs['src']
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, features="html.parser")
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])
    
