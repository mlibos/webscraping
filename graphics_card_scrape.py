from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import pandas


filename = 'products.csv'
f = open(filename,'w')
headers = 'brand, product_name, price, shipping\n'
f.write(headers)
url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"
uclient = ureq(url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html,'html.parser')
containers = page_soup.findAll('div',{'class':'item-container'})
for container in containers:
	brand = container.div.div.a.img['title']
	title = container.findAll('a',{'class':'item-title'})[0].text
	price_class = container.findAll('ul',{'class':'price'})[0]
	price = price_class.findAll('li',{'class':'price-current'})[0].strong.text
	shipping = container.findAll('li',{'class':'price-ship'})[0].text.strip()
	f.write(brand+',' + title.replace(',','|') + ',' + price + ',' + shipping + '\n')
f.close()

df_product = pandas.read_csv(filename)
print(df_product)

