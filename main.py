import requests
import bs4
import lxml
import random
import time
from pymongo import MongoClient
import app.config

# Setup Database
client = MongoClient()
db = client.jobsearch


CONFIG = 'site.yaml'
site_url = app.config.get_site_url( app.config.set_settings(CONFIG))
company_base_url = 'https://www.offerzen.com'


def get_page(url):
    res = requests.get(url)
    return bs4.BeautifulSoup(res.text, 'lxml')


def save_page_data(page_name, page_data):
    key_name = page_name.replace(".", "@")
    page = {key_name: page_data}
    return db.pages.insert_one(page)


def get_main_page_links(page):
    url = []
    for link in page.find_all('a', class_='company'):
        url.append(link.get('href'))
    return url


def get_company_data(url_list):
    count = 0
    for link in url_list:
        url = company_base_url + link
        page = get_page(url)
        result = save_page_data(link, page)
        print(result.inserted_id)
        count = count + 1
        time.sleep(1)
    return count


def process_company_link(page):
    for link in page.find_all('a', class_='company'):
        company = {}
        link_attributes = link.attrs
        elevator_pitch = link.select('elevator-pitch')
        item_info = []
        for detail in link.select('.co-item'):
            item_info.append(detail.get_text())


def get_main_page():
    main_page = get_page(site_url)
    result = save_page_data(site_url, main_page)
    print(result.inserted_id)
    return main_page


# get list of links
def main():
    main_page = get_main_page()
    company_links = get_main_page_links(main_page)
    random.shuffle(company_links)
    result = get_company_data(company_links)


if __name__ == '__main__':
    main()
