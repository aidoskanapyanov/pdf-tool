from pathlib import Path

import typer
from rich import print

from .commands.docs import app as docs_app

app = typer.Typer()
app.add_typer(docs_app, name="docs", help="Generate documentation")


def list_current_dir():
    return [str(dir) for dir in Path(".").iterdir()]


@app.command()
def ls():
    """
    List files in current directory
    """
    dirs = list_current_dir()
    dirs.sort()

    typer.echo("Listing files in current directory:\n")
    print(dirs)
