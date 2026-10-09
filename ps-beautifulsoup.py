from bs4 import BeautifulSoup
import requests
import os
import re

url = "http://127.0.0.1/pluralsight/sample.html"
website = requests.get(url)
bf4_web = BeautifulSoup(website.text, "lxml")

products = bf4_web.find_all(class_="product")
#pattern = re.compile("\bproduct\b")
#product_results = pattern.search(website.text)

for product in products:
    prod_details = str(product).split("<br/>")
    print("------------------------------------------")
    with open(prod_details[0][47:-3].split("/")[2], 'wb') as pic:
        pic_add = requests.get("http://127.0.0.1/pluralsight/" + prod_details[0][47:-3])
        pic.write(pic_add.content) 
    print("Image scraped: " + prod_details[0][47:-3])
    print("Product Name: " + prod_details[1][2:])
    print("Product Amount: " + prod_details[2][2:])
