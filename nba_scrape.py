from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import pandas

url = 'https://www.basketball-reference.com/leagues/NBA_2021_advanced.html'
uclient = ureq(url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html,'html.parser')
table_container = page_soup.findAll('div',{'class':'table_container'})[0]
stats = table_container.findAll('pre',{'id':'csv_advanced_stats'})
print(stats)