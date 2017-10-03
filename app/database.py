from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.jobsearch


# Save page data into mongo
def save_page_data(page_name, page_data):
    key_name = page_name.replace(".", "@")
    data = page_data.text
    page = {'key': key_name, 'page': data}
    return db.pages.insert_one(page)


# Find page via key with search text
def find_page(search_text):
    document = db.pages.find_one({'$text': {'$search': search_text}}, {"key": 1})
    return document


# retrieve page with object id
def retrieve_page(page_id):
    document = db.pages.find_one({"_id": ObjectId(page_id)}, {"page": 1})
    return document


# save company data
def save_company_data(name, data):
    company = {
        'name': name,
        'detail': data
    }
    return db.company.insert_one(company)


def update_company_data(company_id, data):
    pass


def retrieve_company_by_href(search_text):
    company = db.companies.find_one({'$text': {'$search': search_text}})
    return company


#companies
# _id
# company
# elevator-pitch
# details
# data-id
# data-search
# data-cities
# tech-stack
# href
#pages
# _id
# key
# page
