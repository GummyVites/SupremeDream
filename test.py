from urllib2 import urlopen
from bs4 import BeautifulSoup
from splinter import Browser
import time
import sys

name = "Danny wong"
email = "KevinLee@gmail.com"
phone = "3333333333"
address = "1600 field day tissue"
zip = "20000"
state = "CA"
cctype = "master"  
ccnum = "1111111111111111"  
ccmonth = "11"  
ccyear = "2025"  
cccvc = "111"  
city = "porter"

checkoutUrl = "https://www.supremenewyork.com/checkout"
product = "Silk Polo"
color = "Black"
link =""
link2= ""
supremenewyork = "http://www.supremenewyork.com"
itemUrl = ""
url = ""

html = urlopen("http://www.supremenewyork.com/shop/all/shirts")
bsObj = BeautifulSoup(html, "html.parser")

for image in bsObj.findAll('a'):
	if(product in image):
		link = image['href']
	if (color in image):
		link2 = image['href']
	if(link == link2):
		itemUrl = supremenewyork + link2

url = itemUrl
browser = Browser('chrome')
browser.visit(url)
browser.find_option_by_text("Small").first.click()
browser.find_by_name('commit').click()
time.sleep(0.2)
browser.visit(checkoutUrl)
browser.fill("order[billing_name]", name)
browser.fill("order[email]", email)
browser.fill("order[tel]", phone)
browser.fill("order[billing_address]", address)
browser.fill("order[billing_zip]", zip)
browser.fill("order[billing_city]", city)
browser.select("order[billing_state]", state)
browser.select("credit_card[type]", cctype)
browser.fill("credit_card[cnb]", ccnum)
browser.select("credit_card[month]", ccmonth)
browser.select("credit_card[year]", ccyear)
browser.fill("credit_card[vval]", cccvc)
