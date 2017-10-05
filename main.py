#!/usr/bin/env python

import click
import app


@click.group()
def retrieve():
    pass


@retrieve.command()
def download_company_list():
    app.retrieve.retrieve_pages()


@retrieve.command()
def process_company_list():
    app.home.main()


@retrieve.command()
def get_home_pages():
    query = app.database.find_companies_by_missing_field('home_page')
    app.company.get_company_home_pages(query)


cli = click.CommandCollection(sources=[retrieve])

if __name__ == '__main__':
    cli()
