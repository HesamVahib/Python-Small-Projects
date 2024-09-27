import pymysql
import requests
from bs4 import BeautifulSoup

# Setup database connection
cnx = pymysql.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="python",
)
cursor = cnx.cursor()

# Getting data from the website
txt = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = BeautifulSoup(txt.text, 'html.parser')
    
# Finding countries blocks and put them in a list
blocks = soup.find_all('div', attrs={'class' : 'col-md-4 country'})

# Navigating in country block to extract each country's data
for  i, country_block in enumerate(blocks):
    if i >= 20:
        print('COMPELETED!, All data is already enetered.') # Success Message
        break;  # Stop entering data by 20th country
    
    # Finding each country's specification
    name = country_block.find('h3').text.strip()
    capital = country_block.find('span', attrs={'class' : 'country-capital'}).text.strip()
    population = country_block.find('span', attrs={'class' : 'country-population'}).text.strip()
    area = country_block.find('span', attrs={'class' : 'country-area'}).text.strip()

    # Pushing the data into the database
    query = 'INSERT INTO country_info (name, capital, population, area) VALUES (%s, %s, %s, %s)'
    data = (name, capital, population, area)
    cursor.execute(query, data)
    cnx.commit()

cnx.close()
