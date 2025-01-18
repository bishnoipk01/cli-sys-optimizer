
import click
from optimizer.system_operations import clean_temp_files, optimize_disk
from optimizer.process_manager import list_processes, kill_process
from optimizer.startup_manager import list_startup_programs, disable_startup_program
from optimizer.monitor import display_resources
from optimizer.suggest import get_suggestions

@click.group()
def cli():
    """Optimizer CLI: A system optimization tool"""
    print("Welcome to the Optimizer CLI")
    print("--------------------------------")

@cli.command()
def clean():
    """Clean temporary files."""
    click.echo("Cleaning temporary files...")
    clean_temp_files()

@cli.command()
def optimize():
    """Optimize disk usage."""
    click.echo("Optimizing disk usage...")
    optimize_disk()

@cli.command()
def monitor():
    """Monitor system resources in real-time."""
    display_resources()

@cli.command()
def suggest():
    """Provide optimization suggestions."""
    suggestions = get_suggestions()
    for suggestion in suggestions:
        print(suggestion)

@cli.command()
@click.option('--name', required=True, help='Name of the process to kill.')
def kill(name):
    """Kill a process by name."""
    click.echo(f"Attempting to kill process: {name}")
    kill_process(name)

@cli.command()
def list_process():
    """List all running processes."""
    click.echo("Listing all running processes...")
    list_processes()

@cli.command()
def list_startup():
    """List all startup programs."""
    click.echo("Listing all startup programs...")
    list_startup_programs()

@cli.command()
@click.option('--name', required=True, help='Name of the startup program to disable.')
def disable_startup(name):
    """Disable a startup program."""
    click.echo(f"Disabling startup program: {name}")
    disable_startup_program(name)

if __name__ == "__main__":
    cli()
