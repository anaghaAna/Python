import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.cet.ac.in/head-of-departments/")

source_code=req.content
soup=BeautifulSoup(source_code,"lxml")
figure_element=soup.find("figure",class_="wp-block-table")
table=figure_element.find("table")

table_rows=table.find_all("tr")
table_rows=table_rows[1:]

for row in table_rows:
        tds = row.find_all("td")
        name = tds[0].text
        department=tds[1].text
        number=tds[2].text
        print(name,department,number)
        