# -*- coding: utf-8 -*-
"""Untitled1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q14H67pDbI6_jTnGmBUQPbsx8ksXyfPH
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
url="https://islamqa.info/en/answers/128927/it-is-essential-to-acquire-and-take-possession-of-items-before-selling-them"
page=requests.get(url)
page
soup=BeautifulSoup(page.content,"html5")
title=soup.find(class_="title is-4 is-size-5-touch")
print(title.text)
question=soup.find(class_="single_fatwa__question text-justified")
print(question.text)
answer=soup.find(class_="single_fatwa__answer")
print(answer.text)

data=[[title,question,answer]]
df=pd.DataFrame(data,columns=["title","question","answer"])
print(df)
df.to_csv("scrapping.csv")
print("ok")