import typer
from .commands.docs import app as docs_app

app = typer.Typer()
app.add_typer(docs_app, name="docs", help="Generate documentation")


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")


@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")
