import bs4
import lxml
from . import database as db


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


# Parse page with BeautifulSoup
def parse_page(page):
    return bs4.BeautifulSoup(page, 'lxml')


class Company:
    pass
