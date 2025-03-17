import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def get_cities_name(urls_to_iterate) : 
    print('getting city names .', end=' ')
    cities_names = []
    for url in urls_to_iterate : 
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        breadcrumb_nav = soup.find("nav", class_="breadcrumb")
        breadcrumb_items = breadcrumb_nav.find_all("a", class_="breadcrumb_link")
        city_name = breadcrumb_items[2].span.text            
        cities_names.append(city_name)
        print('.', end=' ', flush=True)
    print()
    return cities_names