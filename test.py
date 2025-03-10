# find closest border to long and lat to when html_instructions say "crossing to united states"
# find info from official website of how long it'll take (calculating based on when the person will arrive at the border)
# find time from origin to border + border to destination + total time from before
# suggest the new best route based on these options
import googlemaps 
import html
from bs4 import BeautifulSoup # CANNOT DO USING BEAUTIFULSOUP!!!!!!!!!!!!!
import requests
url = 'https://bwt.cbp.gov' 
response = requests.get(url)
if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'lxml')
    # title_tag = soup.find('body').find('app-root').find('app-home').find('div', class_='col-xs-12 col-sm-12 col-md-12 col-lg-12').find('div', class_='container-fluid').find('div', class_='row').find('div', class_='row').find('div', class_='col-xs-12 col-sm-6 col-md-6 col-lg-6').find('div', class_='col-xs-12 col-sm-6 col-md-6 col-lg-6').find('ul', class_='dropdown-menu scrollable-menu').find('li').find('a', class_='dropdown-item')
    title_tag = soup.find('ul', class_='dropdown-menu scrollable-menu').find('li').find('a', class_='dropdown-item')
    print(title_tag.text)
    # print("Title:", title_tag.text.strip())
    # a = soup.find_all('div')
    # print(a)
    # border = soup.find_all('ul', class_='dropdown-menu scrollable-menu')
    # print(border)
else:
    print('nah sh didnt work')
