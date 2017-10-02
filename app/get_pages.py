import requests
import bs4
import lxml
import random
import time
from . import config as app_config
from . import database

db = database.db

CONFIG = app_config.CONFIG_DATA
site_url = app_config.get_site_url(app_config.set_settings(CONFIG))
company_base_url = app_config.BASE_URL


def get_page(url):
    return requests.get(url)


# parse the page with beautfile soup
def get_page_parsed(res):
    return bs4.BeautifulSoup(res.text, 'lxml')


# Save page data into mongo
def save_page_data(page_name, page_data):
    key_name = page_name.replace(".", "@")
    data = page_data.text
    page = {key_name: data}
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


def get_main_page():
    main_page = get_page(site_url)
    result = save_page_data(site_url, main_page)
    print(result.inserted_id)
    return main_page


# get list of links
def retrieve_pages():
    main_page = get_main_page()
    parsed_page = get_page_parsed(main_page)
    company_links = get_main_page_links(parsed_page)
    random.shuffle(company_links)
    result = get_company_data(company_links)
    print(result)


def main():
    pass


if __name__ == '__main__':
    main()
