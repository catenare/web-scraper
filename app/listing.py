from . import get_pages
from . import database as db

def retrieve_main_page():
    pass


def process_company_link(page):
    for link in page.find_all('a', class_='company'):
        company = {}
        link_attributes = link.attrs
        elevator_pitch = link.select('elevator-pitch')
        item_info = []
        for detail in link.select('.co-item'):
            item_info.append(detail.get_text())


def main():
    pass


if __name__ == '__main__':
    main()
'''
Retrieve the main page from the database.
Get all the information from the a tag for each company
Create new collection/table with just the company information
href link as the id to find the individual company in the collection of company information.

'''
