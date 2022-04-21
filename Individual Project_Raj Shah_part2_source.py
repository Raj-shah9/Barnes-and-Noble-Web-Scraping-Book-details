#!/usr/bin/env python
# coding: utf-8

# In[1]:

## Importing the required libraries and initiliazing counts
from bs4 import BeautifulSoup
import requests
import time
import re
from random import randint
from time import sleep
count = 0
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
"authority": "www.tagesschau.de",
"method": "GET",
"path":"/",
"scheme":"https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9,de;q=0.8",
"cache-control": "max-age=0",
"cookie": "atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%2257ea5dd6-4c35-4982-942f-8a7f8b8c3a4b%22%2C%22options%22%3A%7B%22end%22%3A%222023-02-17T05%3A02%3A59.936Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-595936-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D",
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1"}

#Defining functions

def saveString(html, filename="test.html"):
    try:
        file = open(filename,"w",encoding='utf-8')
        file.write(str(html))
        file.close()
    except Exception as ex:
        print('Error: ' + str(ex))

def loadString(f="test.html"):
	try:
		html = open(f, "r", encoding='utf-8').read()
		return(html)
	except Exception as ex:
		print('Error: ' + str(ex))



# In[31]:

# Finding the first 40 books on Barnes and Noble
URL = 'https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=40&page=1'
pages = requests.get(URL , headers= header)
docs = BeautifulSoup(pages.content, "html.parser")
Links = docs.find_all('h3', class_="product-info-title")

# Getting the details of each book from their respective pages and saving them into an offline file
for number in range(0,40):
    find_a = Links[number].find('a')['href']
    URL = requests.get('https://www.barnesandnoble.com/'+ find_a, headers = header)
    Page = BeautifulSoup(URL.content,"html.parser")
    saveString(Page,filename = 'Books' + str(number) + '.html' )
    sleep(randint(10,20))


# In[56]:


# Loading the data
for page in range(0, 40):
    loaded_page = loadString('Books'+ str(page) +'.html')
    doc = BeautifulSoup(loaded_page, "lxml")
    Title_of_book =doc.find('h1',class_="pdp-header-title text-lg-left text-sm-center mr-md-l ml-md-l mr-sm-l ml-sm-l").text
    divisions = doc.find('div', class_='overview-cntnt').text[0:100]
    print('Title: ' + Title_of_book)
    print(divisions)
    print('')
    print('')

# Getting the desired items
    for boxes in divisions:
        try :

            Titles = boxes.find('h3', class_="product-info-title").text
            Title_name = Titles.find('a', class_=' ')[product-title-plp].text
            print(Titles)

            Linkbox = boxes.find('a', class_ = 's-item__link')['href']
            if Titles: print("The link for this item is:",Linkbox)

            Bids = boxes.find('span', class_='s-item__bids s-item__bidCount').text
            print("The number of bids for this item are",Bids)

            print('')
        except Exception as ex :
            pass

