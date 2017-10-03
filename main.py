import click
import app


def main():
    print(app.get_pages.company_base_url)
    print(app.get_pages.site_url)
    app.get_pages.retrieve_pages()


if __name__ == '__main__':
    main()
