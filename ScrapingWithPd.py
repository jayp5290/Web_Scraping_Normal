import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=mobiles&_sacat=0"


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        products = {
            'title': item.find('h3', {'class': 's-item__title'}).text,
            'soldprice': float(item.find('span', {'class': 's-item__price'}).text.replace('$', '').replace(' ''').strip()),
            'soldproducts': item.find('span', {'class': 's-item__hotness s-item__itemHotness'}).find('span',{'class': 'BOLD'}.text),
            'link': item.find('a', {'class': 's-item__link'})['href'],
        }
        productslist.append(products)  # print(products)
    return productslist


def output(productlist):
    productsdf = pd.DataFrame(productlist)
    productsdf.to_csv('output.csv', index=False)
    print('saved to CSV')
    return


soup = get_data(url)
parse(soup)
