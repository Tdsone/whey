import typer

cli = typer.Typer()


@cli.command()
def hi():
    typer.echo("Hello World")
