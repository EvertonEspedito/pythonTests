import re
 
import requests
from bs4 import BeautifulSoup
 
url = 'https://evertonespeditoportifolio.vercel.app/'
response = requests.get(url)
raw_html = response.text
# print(raw_html)
parsed_html = BeautifulSoup(raw_html, 'html.parser')
# print(parsed_html.title)

aboutDev = parsed_html.select_one('#fh5co-about > div > div.center > div')
# print(aboutDev.text)
toTextAbout = ""
for p in aboutDev.select('p'):
    toTextAbout += re.sub(r'\s{1,}',' ',p.text)

with open("sobre.txt", "w", encoding="utf-8") as f:
    f.write(toTextAbout)

servicesDev = parsed_html.select_one('#fh5co-features > div > div')
toTextServices = ""
for p in servicesDev.select('p'):
    toTextServices += re.sub(r'\s{1,}',' ',p.text)

with open("servicos.txt", "w", encoding="utf-8") as f:
    f.write(toTextServices)
