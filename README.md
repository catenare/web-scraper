# Web Scraper for list of companies from OfferZen
* Download company information to customize how I process it.
* Use as a commandline client to process parts as necessary.

## Using..
* Framework
    * ~~ [Scrapy](https://docs.scrapy.org/en/latest/index.html) - Framework for scraping a website ~~
    * ~~pip install --user Scrapy~~
* Libraries
    * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
    * [Requests](http://docs.python-requests.org/en/master/)
    * [click](http://click.pocoo.org/5/) - create commandline interface for package
    * [Yaml](http://yaml.readthedocs.io/en/latest/) - store config info in yaml file
    * time - sleep
    * random - shuffle list of links
* Database
    * [Mongod](https://www.mongodb.com/) - using mongo for data storage.

## Environment
* [Virtualenv](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) - Using Virtualenvwrapper.
    * Explicitly using python36
    * `makevirtualenv -a . -p python36 jobscraper`
* Starting out with Requests, BeautifulSoup4 and saving in MongoDb.
* Install package - `pip install beautifulsoup4 requests pymongo lxml`

## Setup
* Config settings
    * Use *ruamel.yaml* for reading YAML file.

## Issues
* UTF-8 errors when trying to save result of BeautifulSoup page.
    * Save the request.text response instead. No need to tranform with BeautifulSoup yet.

## Flow
1. ~~Download main page with links to all the company pages~~
    1. ~~Save page as request.text in mongodb~~
    1. ~~Parse the main page to get links for all the companies~~
1. ~~Using links from main page, download individual company pages.~~
1. ~~Save pages in mongodb~~
1. Process company details
    1. From main page
        1. City option list
        1. Technology option list
        1. Individual company info:
            * Elevator pitch
            * Location
            * Company Size
            * Technologies
            * City category - data-cities
            * Technology stack - data-tech-services
            * Company Id - data-id
    1. Retrieve information
        1. Company name
        1. Company url
        1. Company stack
        1. Company address/location
