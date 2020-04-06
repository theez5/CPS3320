#By leveraging the BeautifulSoup library, we can effectively webscrape websites to obtain specific information.
#This program webscrapes the weather.gov website, formats the results into a dataframe via pandas.
#Then, the temperature data for the 7 days is plotted on a line graph.

import requests
from bs4 import BeautifulSoup
import pandas as p
import matplotlib.pyplot as plt

#link to product page
productPage = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.3732&lon=-74.1712#.XnwXl4hKiUk')
#scraping the contents of the url page
content = BeautifulSoup(productPage.content, 'html.parser')
#locating the proper div which contains the seven day forecast
week = content.find(id='seven-day-forecast-list')
#grabbing the div with each unique day in the list
days = week.find_all(class_='tombstone-container')

period_names = [day.find(class_='period-name').get_text() for day in days]
short_desc = [day.find(class_='short-desc').get_text() for day in days]
temp = [day.find(class_='temp').get_text() for day in days]


formatweather = p.DataFrame({
    'Day: ' : period_names,
    'Forecast: ' : short_desc,
    'Temperatures: ' : temp
})

#extracting integers from string
res = formatweather['Temperatures: '].str.extract('(\d+)').astype(int)

#find the average of all temperatures in 7 day forecast
avg = res[0].mean()

#extracting days of week
days = formatweather['Day: ']

#plot temperatures and days of the week
plt.plot(days,res)
plt.xlabel("Day of Week")
plt.ylabel("Temperature in Farenheit")
plt.show()

