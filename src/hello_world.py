'''
a sample of sphinx-click documentation
'''

import click


@click.group()
def greet():
    """A sample command group."""
    pass

@greet.command(help="hello message")
@click.argument('user', envvar='USER')
def hello(user):
    """Greet a user."""
    click.echo('Hello %s' % user)

@greet.command(help="message to all over the world")
def world():
    """Greet the world."""
    click.echo('Hello world!')