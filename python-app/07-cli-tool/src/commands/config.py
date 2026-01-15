import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def show():
    """Show configuration"""
    console.print("[bold]Current Configuration:[/bold]")
    console.print("  Environment: development")
    console.print("  Debug: True")
