from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
import sys

r = requests.get("http://www.supremenewyork.com/shop/all").text
parse = requests.get("http://www.supremenewyork.com/shop/all").text
supreme = "http://www.supremenewyork.com"
productCategoery = "jackets"
color = "Black"
productName = "Shadow Plaid Wool Overcoat"
link2 =""
link3 =""
itemUrl=""
checkoutUrl = "https://www.supremenewyork.com/checkout"
name = "Kevin Lee"
email = "KevinLee@gmail.com"
phone = "3333333333"
address = "1600 field day tissue"
zip = "20000"
state = "CA"
cctype = "master"  
ccnum = "8325802169636318"  
ccmonth = "06"  
ccyear = "2019"  
cccvc = "800"  
city = "porter"






soup = BeautifulSoup(parse, "html.parser")

for a in soup.find_all('a', href=True):
    #print "Found the URL:", a['href']
    link = a['href']
    #print link
    if productCategoery in link:
    	prdurl = supreme + link
    	#print prdurl

    	requests2 = requests.get(prdurl).text
    	soup2 = BeautifulSoup(requests2, "html.parser")

        for b in soup2.find_all('a', class_=True):
        	print b
        	if productName in b:
        		link2 = b['href']
        		#print link2
        	if color in b:
        		link3 = b['href']
        		#print link3
        	if link2 == link3:
        		itemUrl = supreme + link2
        		#print itemUrl
        		#print link2
        		#print link3
        		#print supreme

browser = Browser('chrome')
url = itemUrl
#print url
browser.visit(url)
browser.find_option_by_text("Large").first.click()
browser.find_by_name('commit').click()
time.sleep(0.2)
browser.visit(checkoutUrl)
browser.fill("order[billing_name]", name)
browser.fill("order[email]", email)
browser.fill("tl", phone)
browser.fill("order[billing_address]", address)
browser.fill("order[billing_zip]", zip)
browser.fill("order[billing_city]", city)
browser.select("order[billing_state]", state)
browser.select("credit_card[type]", cctype)
browser.fill("credit_card[cnb]", ccnum)
browser.select("credit_card[month]", ccmonth)
browser.select("credit_card[year]", ccyear)
browser.fill("credit_card[vval]", cccvc)
#browser.find_by_css('.terms').click()
#browser.find_by_name('commit').click()  
#sys.exit(0)
        		

	



