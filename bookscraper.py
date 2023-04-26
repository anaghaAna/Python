import requests
from bs4 import BeautifulSoup
URL="http://books.toscrape.com/"
req=requests.get(URL)
source_code=req.content
soup=BeautifulSoup(source_code,'lxml')
print(soup)
article=soup.find_all('article')
for i in article:
    h3 = i.find('h3')
    a = h3.find('a')
    name = a.text
    print(name)
    #Find price
    price=i.find('div',class_="product_price")
    price=price.find('p')
    price=price.text[1:]
    price=float(price)
    if price<50:
        with open('books.txt','a') as file:
            file.write(name + " : "+ str(price) + "\n") 
    
    