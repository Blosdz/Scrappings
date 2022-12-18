import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
from urllib.request import Request,urlopen
import numpy as np


URL = input()

# items= results.find_all("div", class_="icbu-product-card")
response=Request(URL,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.106'})

webpage=urlopen(response).read()
# file=open("parse_data.txt","w")
page_soup=BeautifulSoup(webpage,"html.parser")

results=page_soup.find("div",class_="sr-layout-block ")
items=page_soup.find_all("div",class_="prod-item-inner")

fileNumber=np.random.randint(low=1,high=100,size=7);

file=open("parc_data"+str{fileNumber}+.txt","w")
 
# file=open("test.txt",mode="w",encoding="utf-8")

for item in items:
    name_element=item.find("div",class_="prod-title")
    unit_price_element=item.find("span",class_="value")
    # print(name_element.text)
    # print(unit_price_element.text)
    # file.write(name_element.text)   
    file.write((name_element.text).strip())
    file.write(" |  | ")
    file.write(unit_price_element.text)
    file.write("\n")
        

file.flush
# for item in items:
    # name_element=item.find("span",class_="title-con")
    # unit_price_element=item.find("span",class_="num")
    # print(name_element.text)
    # print(unit_price_element.text)
    # file.write(name_element.text)
    # file.write(" |  | ")
    # file.write(unit_price_element.text)
    # file.write("\n")
# file.flush
