import typer
from rich.console import Console
from commands import user, config

app = typer.Typer(help="CLI Tool Application")
console = Console()

app.add_typer(user.app, name="user", help="User management commands")
app.add_typer(config.app, name="config", help="Configuration commands")

@app.command()
def hello(name: str = typer.Option("World", help="Name to greet")):
    """Say hello"""
    console.print(f"[bold green]Hello {name}![/bold green]")

@app.command()
def version():
    """Show version"""
    console.print("[bold blue]CLI Tool v1.0.0[/bold blue]")

if __name__ == "__main__":
    app()
