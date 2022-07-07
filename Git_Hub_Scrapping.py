from asyncio.windows_events import NULL
from cgi import print_arguments
from cmath import pi
from importlib.resources import contents
from operator import le
from urllib import response
from bs4 import BeautifulSoup
from hyperlink import URL
import requests
import pandas as pd


URL = 'https://github.com/topics'
r = requests.get(URL)

st_code = r.status_code
if st_code != 200:
    print("Main Page request Failed kindly check you internet connectivity")
else:
    print('Main page Request Success ...')
    print('')

    page_text = r.text
    # print(len(page_text))

    soup = BeautifulSoup(page_text, 'html.parser')
    # print(soup.prettify())

    Heading_class = 'f3 lh-condensed mb-0 mt-1 Link--primary'
    Heading_Discription_class = 'f5 color-fg-muted mb-0 mt-1'
    Heading_Link_Class = 'no-underline flex-grow-0'
    Heading_Basic_URL = 'https://github.com'
    Heading_Star_ID = 'repo-stars-counter-star'

    Heading_name = soup.find_all('p', class_ = Heading_class)
    Heading_Discription = soup.find_all('p', class_ = Heading_Discription_class)
    Heading_Links = soup.find_all('a', class_ = Heading_Link_Class)

    # print(len(Heading)) # Total number of heading in a list

    Heading_name_list = []
    Heading_Discription_list = []
    Heading_Links_list = []
    Heading_Stars_list = []

    for n in range(len(Heading_name)):
        Heading_name_list.append(Heading_name[n].text)
        Heading_Discription_list.append(Heading_Discription[n].text)
        Heading_Links_list.append(Heading_Basic_URL+Heading_Links[n]['href'])


#############################################
        inside_r = requests.get(Heading_Links_list[n])
        if inside_r.status_code >= 200 and inside_r.status_code <= 299:
            print(f'{n+1}th sub page Request Success')
            inside_page_star  = inside_r.text
            inside_soup = BeautifulSoup(inside_page_star, 'html.parser')
            stars = inside_soup.find('span', id = Heading_Star_ID).text
            Heading_Stars_list.append(stars)
        else:
            print(f'{n+1}th sub page Request Failed')



all_in_one = {
    "Heading Name": Heading_name_list,
    "Obtained Stars": Heading_Stars_list,
    "Heading Links" : Heading_Links_list,
    "Heading Discription" : Heading_Discription_list
}

df = pd.DataFrame(all_in_one)
df.to_csv("Record.csv")