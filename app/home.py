from . import database as db
from . import company


HOME_PAGE_SEARCH_TEXT = "offerzen"
CITY = 'city'
TECH = 'tech-services'
KEY_INDEX = "key"


class Home(company.Page):

    def get_main_page_links(self):
        page = self.get_parsed_page()
        url_list = []
        for link in page.find_all('a', class_='company'):
            link_info = {
                'company': get_company(link),
                'elevator-pitch': get_elevator_pitch(link).get_text(strip=True),
                'details': get_details(link).get_text("|", strip=True),
                'data-id': link['data-id'],
                'data-search': link['data-search'],
                'data-cities': link['data-cities'],
                'tech-stack': link['data-tech-services'],
                'href': link['href']
                # 'anchor': self.get_anchor(link['href'])
            }
            try:
                anchor = self.get_anchor(link['href'])
            except IndexError as err:
                print("error finding href: {} {}".format( link_info['company'], err))
            else:
                link_info['anchor'] = anchor
                url_list.append(link_info)
        return url_list

    def get_city_links(self):
        return self.get_option_list(CITY)

    def get_stack_links(self):
        return self.get_option_list(TECH)

    def get_option_list(self, css_id):
        page = self.get_parsed_page()
        select = page.find(id=css_id)
        link = []
        for option in select.find_all('option'):
            if '' != option['value']:
                link.append({'value': option['value'], 'text': option.text})
        return link

    def get_anchor(self, href):
        record = db.find_company_page(href)
        comp = company.Company(record)
        return comp.get_anchor()

    def save_info(self):
        cities = self.get_city_links()
        stack = self.get_stack_links()
        companies = self.get_main_page_links()

        city_result = db.db.options.insert_one(
            {'cities': cities}
        )
        stack_result = db.db.options.insert_one(
            {'stack': stack}
        )
        company_result = db.db.companies.insert_many(
            companies
        )
        return {
            'cities': city_result,
            'stack': stack_result,
            'companies': company_result
        }


def get_company(anchor):
    return anchor.h3.string


def get_elevator_pitch(anchor):
    return anchor.find(class_='elevator-pitch')


def get_details(anchor):
    return anchor.find(class_='co-details')


def main():
    index_result = db.create_index_on_pages(KEY_INDEX)
    print('index result: {}'.format(index_result))
    page = db.find_page(HOME_PAGE_SEARCH_TEXT)
    main_page = Home(page)
    result = main_page.save_info()
    return result
