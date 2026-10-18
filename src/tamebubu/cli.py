# src/tamebubu/cli.py
import typer

app = typer.Typer(help="Spaced practice for procedural skills.")


@app.command()
def practice() -> None:
    """Start a practice session."""
    typer.echo("practice loop goes here")


@app.command()
def stats() -> None:
    """Show attempts and accuracy."""
    typer.echo("stats go here")
