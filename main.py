import click
import app


@click.command()
def main():
    click.echo(app.get_pages.CONFIG)
    click.echo(app.get_pages.site_url)


if __name__ == '__main__':
    main()
