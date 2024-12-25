# cli entry point of application

import click
from optimizer import monitor, suggest, actions, profile

@click.group()
def cli():
    """CLI System Resource Optimizer"""
    print('--------------------------------')

@cli.command()
def monitor_resources():
    monitor.display_resources()

@cli.command()
def suggest_optimization():
    suggestions = suggest.get_suggestions()
    for suggestion in suggestions:
        click.echo(suggestion)
    
@cli.command()
@click.argument("action")
def perform_action(action):
    """ Perform optimization actions """
    actions.execute_action(action)

@cli.command()
@click.argument("profile_name")
def apply_profile(profile_name):
    """ Apply a predefined profile """
    profile.apply_profile(profile_name)

if __name__ == "__main__":
    cli()