---
layout: image-right
image: https://media.gettyimages.com/id/104737255/fr/photo/winning-african-american-boxer-in-boxing-ring.jpg?s=612x612&w=0&k=20&c=2SWGnVhZz_ftKM27-kQmnzFuccwZ2NIOPCJb8OtWvz0=
---

# Le favori des bookmakers : **click**

<v-clicks>

- 13.6k ⭐
- Used by: 1M repos
- créé par Armin Ronacher (flask, jinja, etc.)
- [Typer](https://typer.tiangolo.com) par @tiangolo (fastapi)

</v-clicks>

---
title: click
layout: center
---

gliss-click.py
```python {1,3,8,13-17|3-6|8-11|13-20}
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
@click.option('--priority', '-p', type=click.Choice(['Low', 'Medium', 'High']), default='Low',
              help='Priority of the issue.')
def create(title, description, priority):
    """Create a new issue."""
    click.echo(f"Creating issue: {title} {description} {priority}")

...

```

---
title: click
layout: center
---

### Génération du --help 
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

---
title: click
layout: center
---

### Aide détaillée sur une commande
```sh
$ python gliss-click.py create --help
Usage: gliss-click.py create [OPTIONS] TITLE

  Create a new issue.

Options:
  -d, --description TEXT          Description of the issue.
  -p, --priority [Low|Medium|High]
                                  Priority of the issue.
  --help                          Show this message and exit.
```
