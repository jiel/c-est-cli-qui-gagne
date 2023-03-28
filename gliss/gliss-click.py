import click


@click.group()
def gliss():
    """Command Line Interface to interact with GitLab Issues."""
    pass

@gliss.command()
def list():
    """List all issues."""
    click.echo("Listing all issues.")

@gliss.command()
@click.argument('title')
@click.option('--description', '-d', help='Description of the issue.')
@click.option('--priority', '-p', type=click.Choice(['Low', 'Medium', 'High']),
              help='Priority of the issue. Valid values are "Low", "Medium", "High".')
def create(title, description, priority):
    """Create a new issue."""
    click.echo(f"Creating issue: {title} {description} {priority}")

@gliss.command()
@click.argument('issue_id', type=int)
def show(issue_id):
    """Show details of an issue."""
    click.echo(f"Showing details of issue: {issue_id}")

@gliss.command()
@click.argument('issue_id', type=int)
def close(issue_id):
    """Close an issue."""
    click.echo(f"Closing issue: {issue_id}")

@gliss.command()
@click.argument('issue_id', type=int)
@click.argument('comment')
def comment(issue_id, comment):
    """Comment on an issue."""
    click.echo(f"Adding comment to issue {issue_id}: {comment}")

@gliss.command()
@click.argument('issue_id', type=int)
@click.argument('assignee_name')
def assign(issue_id, assignee_name):
    """Assign an issue to an assignee."""
    click.echo(f"Assigning issue {issue_id} to {assignee_name}")


if __name__ == '__main__':
    gliss()