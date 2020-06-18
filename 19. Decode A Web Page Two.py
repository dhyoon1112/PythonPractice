import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,features="html.parser")

for text in soup.find_all('p'):
    print(text.get_text())

#print(text.get_text())
