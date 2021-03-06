import requests
import bs4
import lxml
import random
import time
from . import config as app_config
from . import database as db


CONFIG = app_config.CONFIG_DATA
site_url = app_config.get_site_url(app_config.set_settings(CONFIG))
company_base_url = app_config.get_base_url(app_config.set_settings(CONFIG))


def get_page(url):
    result = None
    session = requests.Session()
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36(KHTML, like Gecko) Chrome", "Accept": "text/html,application/xhtml+xml,application/xml; q = 0.9, image / webp, * / *;q = 0.8"}
    result = requests.get(url.strip(), headers=headers, verify=False)
    return result


# parse the page with beautfile soup
def get_page_parsed(res):
    return bs4.BeautifulSoup(res.text, 'lxml')


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
        result = db.save_page_data(link, page)
        print(result.inserted_id)
        count = count + 1
        time.sleep(1)
        print(count)
    return count


def get_main_page():
    main_page = get_page(site_url)
    result = db.save_page_data(site_url, main_page)
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
    print("Welcome to the main retrieve section")


if __name__ == '__main__':
    main()
