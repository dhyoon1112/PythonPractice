import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,features="html.parser")

for link in soup.find_all('h2'):
    print(link.get_text())


#title = soup.find_all('h2')
#print(title.get_text()) #gets all the tags and strings within the text '''

#print(soup.prettify()) #Indents the HTML
