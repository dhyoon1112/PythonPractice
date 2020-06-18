import requests
from bs4 import BeautifulSoup


def text():
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html,features="html.parser")

    text = ''
    for link in soup.find_all('p'):
       text += link.get_text()

    return text

text = text()

with open('file_to_save.txt','w',encoding = 'utf-8') as open_file:
   open_file.write(text)
