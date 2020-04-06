#By leveraging the BeautifulSoup library, we can effectively webscrape websites to obtain specific information.
#This program webscrapes the weather.gov website to output the current 7 day weather forecast into a dataframe.
#The average temperature for the week is also displayed.

import requests
from bs4 import BeautifulSoup
import pandas as p

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

#print("")
print("Here is your 7-day forecast, formatted into a DataFrame with Pandas!")
print(formatweather)

#extracting integers from string
res = formatweather['Temperatures: '].str.extract('(\d+)').astype(int)

avg = res[0].mean()
print("The average temperature this week will be: ",avg,"degrees Farenheit")

