#By leveraging the BeautifulSoup library, we can effectively webscrape websites to obtain specific information.
#This program webscrapes the weather.gov website to output the current weather forecast for the current day.

import requests
from bs4 import BeautifulSoup

#link to product page
productPage = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.3732&lon=-74.1712#.XnwXl4hKiUk')
#scraping the contents of the url page
content = BeautifulSoup(productPage.content, 'html.parser')
#locating the proper div which contains the seven day forecast
week = content.find(id='seven-day-forecast-list')
#grabbing the div with each unique day in the list
days = week.find_all(class_='tombstone-container')

#print results of current day from web scraped results of the seven day forecast
print("Here is today's weather forecast for Holmdel, NJ: ")
print(days[0].find(class_='period-name').get_text())
print(days[0].find(class_='short-desc').get_text())
print(days[0].find(class_='temp').get_text())

