import requests
from  bs4 import BeautifulSoup

URL = 'https://detik.com'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

container = soup.find(("div",{"class":"container"}))

print(container.prettify())



