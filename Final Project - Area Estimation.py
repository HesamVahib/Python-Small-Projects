import pymysql
import requests
from bs4 import BeautifulSoup
from sklearn import tree
import numpy as np

# Database Connection Setup
cnx = pymysql.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="python",
)
cursor = cnx.cursor()

your_table = 'country_info' # Put Your Table Name Here

# Fetching and beautifying data
data = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = BeautifulSoup(data.text, 'html.parser')
countries_name = soup.find_all('h3', attrs={'class': 'country-name'})
countries_info = soup.find_all('div', attrs={'class': 'country-info'})

query = f'INSERT INTO {your_table} VALUES (%s, %s, %s, %s)' # Query to push data into table

# Extractin countries; info and push it to the table
for country, info in zip(countries_name, countries_info):
    name = country.text.strip()
    capital = info.find('span', attrs={'class': 'country-capital'}).text.strip()
    population = info.find('span', attrs={'class': 'country-population'}).text.strip()
    area = info.find('span', attrs={'class': 'country-area'}).text.strip()
    values = (name, capital, population, area)
    cursor.execute(query, values)
cnx.commit()

# Reading population data from database and make them as a suitable input for Machine
cursor.execute(f'SELECT population FROM {your_table};')
data_population = cursor.fetchall()
populationList = list(data_population)
x = [item[0] for item in populationList] # Make integer the variables
x = np.array(x)
x_reshaped = x.reshape(-1, 1) # Make the data as 2D data set

# Reading population data from database and make them as a suitable input for Machine
cursor.execute(f'SELECT area FROM {your_table};')
data_area = cursor.fetchall()
areaList = list(data_area)
y = [item[0] for item in areaList]
y = np.array(y)
y_reshaped = y.reshape(-1, 1)

clf = tree.DecisionTreeClassifier() # Run the Machine
clf = clf.fit(x_reshaped, y_reshaped) # Teach the Machine

new_area = [[int(input('Enter you population: '))]] # Get the population amount to estimate

answer = clf.predict(new_area)
print(f'The estimated area is {answer[0]} KM') # Estimate the area

cnx.close()