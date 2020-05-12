import requests
from bs4 import BeautifulSoup


command=input('do u want to search for something else other than default product(yes/no):')
if command=="yes":
    URL=input('enter the url:')
else:
    URL='https://www.amazon.in/realme-RMA108-Realme-Buds-Wireless/dp/B07XJWTYM2/ref=lp_20954493031_1_1?s=electronics&ie=UTF8&qid=1589096714&sr=1-1'

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[2:3]+price[4:10])
    print(title.strip())
    print('price is=',converted_price )
check_price()
    #if(converted_price<=1799.0):
       # send_mail()
    #print(converted_price)
    #print(title.strip())