from bs4 import BeautifulSoup

import requests
import urllib2

# url = raw_input("Enter the URL\'s from:")

r = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WLrZfSGGPqM")

print(r.status_code)
print(r.content)

# data = r.content

# data = r.text

# soup = BeautifulSoup(data, "html.parser")

# print soup
# print soup.prettify()

# for link in soup.find_all('a'):
#     print(link.get('href'))

# wiki = "https://en.wikipedia.org/wiki/Indonesia"
# page = urllib2.urlopen(wiki)
# soup = BeautifulSoup(page)
