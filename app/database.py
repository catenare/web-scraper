import pymongo
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


def create_index_on_pages(field):
    return db.pages.create_index([(field, pymongo.TEXT)])


def find_company_page(company):
    document = db.pages.find_one({"key": company})
    return document


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


def find_company_by_id(company_id):
    return db.companies.find_one({"_id": ObjectId(company_id)})


def find_companies_by_missing_field(field):
    return db.companies.find({field: {'$exists': False}})


def find_all_companies():
    return db.companies.find()


def update_company_data(company):
    return db.companies.replace_one({'_id': ObjectId(company['_id'])}, company)
