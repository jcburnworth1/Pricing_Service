########## Requests Example ##########
import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.johnlewis.com/john-lewis-partners-hemingway-3-door-sideboard/p230727606'
# < p class ="price price--large" > £260.00 < / p >
TAG_NAME = 'p'
QUERY = {"class": "price price--large"}

response = requests.get(URL)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()

## Regex to extract data
pattern=re.compile(r'(\d+,?\d*\.\d\d)')
match = pattern.search(string_price)
found_price = match.group(1)
without_commas = found_price.replace(',','')
price = float(without_commas)
