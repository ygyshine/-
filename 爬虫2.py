

import requests        #导入requests包
from bs4 import BeautifulSoup
url='https://blog.csdn.net/wei_lin/article/details/102334956'
strhtml=requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#pl_feedlist_index > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > div > div.card-more-a > a')
print(data)         #main > div > div.observe.mode.mtop > div:nth-child(3) > div.centerBox > div.weh.newList > div:nth-child(2) > ul > li:nth-child(1) > a
import re           #pl_feedlist_index > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > div > > a
                    #pl_feedlist_index > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > div > div.card-more-a > a
for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href'),
        'ID': re.findall('\d+', item.get('href'))  #对单一命令生效
    }
print(result)