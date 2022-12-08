from pathlib import Path
from typing import List

import typer
from PyPDF2 import PdfMerger
from rich import print
from rich.progress import track

from .commands.docs import app as docs_app

app = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
)
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


def validate_extensions(pdfs):
    exists = lambda file: file.suffix == ".pdf"
    if not all(map(exists, pdfs)):
        raise typer.BadParameter("Make sure all input files are in PDF format")


def validate_paths(pdfs):
    exists = lambda file: file.exists()
    if not all(map(exists, pdfs)):
        raise typer.BadParameter("Make sure all input files exist.")


def validate_pdfs(pdfs: List[Path]):
    validate_extensions(pdfs)
    validate_paths(pdfs)
    return pdfs


@app.command(no_args_is_help=True)
def merge(
    pdfs: List[Path] = typer.Argument(
        ...,
        help="Input pdf names in a desired order",
        show_default=False,
        callback=validate_pdfs,
    ),
    output_file: str = typer.Argument(
        ...,
        help="Output file name",
        show_default=False,
    ),
):
    """
    Merge pdf files in a specified order
    """

    typer.echo("Merging PDF files:\n")
    merger = PdfMerger()

    for pdf in track(pdfs, description="Processing..."):
        merger.append(pdf)
    merger.write(output_file)
    merger.close()
