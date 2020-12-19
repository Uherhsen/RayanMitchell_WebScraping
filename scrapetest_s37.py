# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:34:52 2020

Навигация по древу синтаксического разбора с 37
для обучения используется:
    http://bit.ly/1KGe2Qk оно же (http://www.pythonscraping.com/pages/page3.html)
    
descendants - потомки, все дочерние элементы 
children - дочерние элементы, ниже на один уровень 
sibling - элементы на одном уровне (дословно братья и сестры)


next_shildren() 

с 41
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, features="html.parser")

for child in bsObj.find("table",{"id":"giftList"}).children: # Выводит список строк с названиями продуктов таблицы, почти аналогичен bsObj.find("table",{"id":"giftList"}).tr
    print(child)
print("\n next_siblings - следующие братья и сестры (не печатает заголовок)\n")
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)

# previous_siblings - предыдущие братья и сестры
# next_sibling - следующ элемент уровня 
# previous_sibling - предыдущий элемент уровня
print("\nПоиск родительских элементов, функции .parent и .parents\n")
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
    
