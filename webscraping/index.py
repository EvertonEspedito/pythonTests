import re
 
import requests
from bs4 import BeautifulSoup
 
url = 'https://www.pichau.com.br/'
response = requests.get(url)
raw_html = response.text
print(raw_html)
parsed_html = BeautifulSoup(raw_html, 'html.parser')
print(parsed_html)