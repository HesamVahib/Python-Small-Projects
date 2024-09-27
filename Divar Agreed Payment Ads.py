import requests
from bs4 import BeautifulSoup

html = requests.get('https://divar.ir/s/tehran?q=%D8%AA%D9%88%D8%A7%D9%81%D9%82%DB%8C')
soup = BeautifulSoup(html.text, 'html.parser')
res = soup.find_all('h2', attrs={'class' : 'kt-post-card__title'})

if res:
    for ad in res:
        print(ad.text)
else:
    print("Error! not found.")

