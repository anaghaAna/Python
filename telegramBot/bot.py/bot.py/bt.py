import asyncio
from config import * 
import telethon
from telethon import TelegramClient,events
import requests
from bs4 import BeautifulSoup

def scrape(URL):
    req=requests.get(URL)
    source_code=req.content
    soup=BeautifulSoup(source_code,'lxml')
    print(soup)
    article=soup.find_all('article')
    for  i in article:
        h3=i.find('h3')
        name=(h3.find('a').text)
        price=i.find('div',class_="product_price")
        price=price.find('p')
        price=price.text[1:]
        price=float(price)
        if price<50:
            with open('books.txt','a')as file:
                file.write(name+":"+str(price)+ "\n")
    return 'books.txt'

async def main():
    bot=await TelegramClient('s',API_ID,API_HASH).start( bot_token=BOT_TOKEN)
    async with bot:
        print("logged in")
        @bot.on(events.NewMessage())
        async def handle_message(event):
            link=event.message.message
            file=scrape(link)
            user_id=event.sender.id
            await bot.send_file(user_id,file)
        await bot.run_until_disconnected()
asyncio.run(main())           
            

asyncio.run(main())

        