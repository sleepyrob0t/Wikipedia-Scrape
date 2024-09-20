# import required modules
import requests
from bs4 import BeautifulSoup
import requests


# get URL
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")

# display status code
print(page.status_code)

# display scraped data
print(page.content)


# get URL
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

# display scraped data
print(soup.prettify())

print('\n\n')
 
# return only text
# does not include HTML tags
print(soup.find_all('p')[0].get_text())