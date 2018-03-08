import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/The_Lumberjack_Song")
html = response.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')

content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.a:
        first_relative_link = element.a.get('href', recursive=False)
        print(first_relative_link)
        break

#print(soup.find(id='mw-content-text').find(class_="mw-parser-output").p.a['href']);

#soup
#print(soup.a)

#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.parent.name)
#print(soup.title.parent)

#rint(soup.div)
#rint(soup.div ['class'])
#rint(soup.div ['id'])

#print(soup.find_all('div'))

#print(soup.find(id="footer-icons"))

#for link in soup.find_all('a'):
#   print(link.get('href'))

#print(soup.get_text())


