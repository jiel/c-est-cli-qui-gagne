---
layout: image-right
image: https://media.gettyimages.com/id/104737255/fr/photo/winning-african-american-boxer-in-boxing-ring.jpg?s=612x612&w=0&k=20&c=2SWGnVhZz_ftKM27-kQmnzFuccwZ2NIOPCJb8OtWvz0=
---

# Le favori des bookmakers : **click**

- 13.6k ⭐
- Used by: 1M repos
- créé par Armin Ronacher (Flask, Jinja, ..)

---
title: click
layout: center
---

gliss-click.py
```python
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

...

```

---
title: click
layout: center
---

```sh
$ python gliss-click.py --help 
Usage: gliss-click.py [OPTIONS] COMMAND [ARGS]...

  Command Line Interface to interact with GitLab Issues.

Options:
  --help  Show this message and exit.

Commands:
  assign   Assign an issue to an assignee.
  close    Close an issue.
  comment  Comment on an issue.
  create   Create a new issue.
  list     List all issues.
  show     Show details of an issue.
```

```sh
$ python gliss-click.py create --help
Usage: gliss-click.py create [OPTIONS] TITLE

  Create a new issue.

Options:
  -d, --description TEXT          Description of the issue.
  -p, --priority [Low|Medium|High]
                                  Priority of the issue. Valid values are
                                  "Low", "Medium", "High".
  --help                          Show this message and exit.
```
