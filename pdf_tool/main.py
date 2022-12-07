from pathlib import Path
from typing import List

import typer
from PyPDF2 import PdfMerger
from rich import print
from rich.progress import track

from .commands.docs import app as docs_app

app = typer.Typer(no_args_is_help=True)
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


@app.command()
def merge(pdfs: List[Path], output_file: str):
    """
    Merge pdf files in a specified order
    """

    typer.echo("Merging PDF files:\n")
    merger = PdfMerger()

    for pdf in track(pdfs, description="Processing..."):
        merger.append(pdf)
    merger.write(output_file)
    merger.close()
