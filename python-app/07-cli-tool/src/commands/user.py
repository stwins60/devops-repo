import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

users = []

@app.command()
def list():
    """List all users"""
    if not users:
        console.print("[yellow]No users found[/yellow]")
        return
    
    table = Table(title="Users")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Email", style="blue")
    
    for idx, user in enumerate(users, 1):
        table.add_row(str(idx), user['name'], user['email'])
    
    console.print(table)

@app.command()
def add(name: str, email: str):
    """Add a new user"""
    users.append({'name': name, 'email': email})
    console.print(f"[green]✓[/green] User {name} added successfully")
