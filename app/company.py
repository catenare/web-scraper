import bs4
import lxml
from datetime import datetime
from . import database as db
from . import retrieve

PAGE = 'page'
KEY = 'key'
ERROR_FILE = 'logs/error'


class Page:
    """ Basic class to represent a page of a company """

    def __init__(self, page_id, key):
        self.id = page_id
        self.key = key
        self.db = db
        self.page = None
        self.parsed_page = None

    def get_key(self):
        return self.key

    def get_id(self):
        return self.id

    def get_page(self):
        if self.page is None:
            page = db.retrieve_page(self.id)
            self.page = page['page']
        return self.page

    def get_parsed_page(self):
        if self.parsed_page is None:
            self.parsed_page = parse_page(self.get_page())
        return self.parsed_page


class Company:
    def __init__(self, record):
        self.record = record
        self.parsed_page = None

    def get_page(self):
        return self.record[PAGE]

    def get_key(self):
        return self.record[KEY]

    def get_parsed_page(self):
        if self.parsed_page is None:
            self.parsed_page = parse_page(self.get_page())
        return self.parsed_page

    def get_anchor(self):
        anchor = self.get_parsed_page().select('div.u-grid-container-3 a')[0]
        return anchor['href']


# get list of companies
def get_company_home_pages(query):
    error_file = ERROR_FILE + datetime.now().strftime('%b_%Y_%H_%M_%f')+".txt"
    error_log = open(error_file, "w")
    for company in query:
        home_page = retrieve.get_page(company['anchor'])
        if home_page is not None:
            company['home_page'] = home_page.text
            result = db.update_company_data(company)
            print('Company updated {} {} {}'
                  .format(company['_id'], company['company'], result.raw_result))
        else:
            print('Error processing company. id: {}, company: {}, url: {}'
                  .format(company['_id'], company['company'], company['anchor']), file=error_log)
    error_log.close()


def list_companies(query):
    for company in query:
        print(company)


# Parse page with BeautifulSoup
def parse_page(page):
    return bs4.BeautifulSoup(page, 'lxml')
