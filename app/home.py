from . import database as db
from . import config
from . import get_pages
from . import company


HOME_PAGE_SEARCH_TEXT = "offerzen"


class Home(company.Page):
    def get_main_page_links(self):
        page = self.get_parsed_page()
        url_list = []
        for link in page.find_all('a', class_='company'):
            url_list.append(link.attrs)
        return url_list


def main():
    page = db.find_page(HOME_PAGE_SEARCH_TEXT)
    main_page = Home(page['_id'], page['key'])
    return main_page
