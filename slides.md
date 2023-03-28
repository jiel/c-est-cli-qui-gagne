---
theme: default
background: https://images.unsplash.com/photo-1552072092-7f9b8d63efcb?fit=crop&w=1920
class: 'text-center'
highlighter: shiki
lineNumbers: false
css: unocss
---

## argparse vs docopt vs click vs fire
# c'est CLI qui gagne ?

Soirée des communautés techniques Rennaises

---

# Command Line Interface

- une IHM qui remonte aux années 60 
- une IHM de choix pour du tooling IT
- avantages :
  - rapidité d'usage (mémoire musculaire)
  - composabilité (scripting)
  - simplicité de développement

---

# définition d'une grammaire

```sh
$ gliss
Usage:
  gliss list
  gliss create <title> [--description=<description>] [--priority=<priority>]
  gliss show <issue-id>
  gliss close <issue-id>
  gliss comment <issue-id> <comment>
  gliss assign <issue-id> <assignee-name>
```

- respect des conventions (POSIX..)
- des arguments et des options logiques et intuitifs
- auto apprentissage avec l'aide intégrée

---

# gliss - another gitlab CLI

```sh
$ gliss --help
gliss - Command Line Interface to interact with GitLab Issues.

Usage:
  gliss list
  gliss create <title> [--description=<description>] [--priority=<priority>]
  gliss show <issue-id>
  gliss close <issue-id>
  gliss comment <issue-id> <comment>
  gliss assign <issue-id> <assignee-name>

Options:
  -h --help                         Show this screen.
  -d --description=<description>    Description of the issue.
  -p --priority=<priority>          Priority of the issue.
                                    Valid values are "Low", "Medium", "High".
```
---


# Le vétéran du circuit: **argparse**

- inclu dans librairie standard depuis python 2.7
- recommandé dans la documentation python (vs [getopt](https://docs.python.org/3/library/getopt.html#module-getopt) et [optparse](https://docs.python.org/3/library/optparse.html))

---

gliss-argparse.py
```python
import argparse

parser = argparse.ArgumentParser(description='Command Line Interface to interact with GitLab Issues.')

subparsers = parser.add_subparsers(title='Commands', dest='command')

# List issues
list_parser = subparsers.add_parser('list', help='List all issues')

# Create new issue
create_parser = subparsers.add_parser('create', help='Create a new issue')
create_parser.add_argument('title', help='Title of the issue')
create_parser.add_argument('--description', help='Description of the issue')
create_parser.add_argument('--priority', choices=['Low', 'Medium', 'High'], default='Low', 
                          help='Priority of the issue')

# Show issue details
show_parser = subparsers.add_parser('show', help='Show details of an issue')
show_parser.add_argument('issue_id', type=int, help='ID of the issue')

...

args = parser.parse_args()
print(vars(args))
```

---

```sh
$ python gliss-argparse.py --help
usage: gliss-argparse.py [-h] {list,create,show,close,comment,assign} ...

Command Line Interface to interact with GitLab Issues.

options:
  -h, --help            show this help message and exit

Commands:
  {list,create,show,close,comment,assign}
    list                List all issues
    create              Create a new issue
    show                Show details of an issue
    close               Close an issue
    comment             Comment on an issue
    assign              Assign an issue to a user
```

---

```sh
$ python gliss-argparse.py create --help
usage: gliss-argparse.py create [-h] [--description DESCRIPTION] [--priority {Low,Medium,High}] title

positional arguments:
  title                 Title of the issue

options:
  -h, --help            show this help message and exit
  --description DESCRIPTION
                        Description of the issue
  --priority {Low,Medium,High}
                        Priority of the issue
```

---


### valeur par défaut
```sh
$ python gliss-argparse.py create "implement create issue" 
{'command': 'create', 'title': 'implement create issue', 'description': None, 'priority': 'Low'}
```

### validation des arguments
```sh
$ python gliss-argparse.py create "implement create issue" --priority=critical
usage: gliss-argparse.py create [-h] [--description DESCRIPTION] [--priority {Low,Medium,High}] title
gliss-argparse.py create: error: argument --priority: invalid choice: 'critical' (choose from 'Low', 'Medium', 'High')
```

### typage
```sh
$ python gliss-argparse.py show 1234                                          
{'command': 'show', 'issue_id': 1234}
```


---

# L'ancienne gloire: **docopt**

- 7.8k ⭐ 
- Used by: 86k repos
- proposé à pycon UK 2012 http://youtu.be/pXhcPJK5cMc
- porté dans 23 langages
- approche recommandée par la [PEP 257](https://peps.python.org/pep-0257/)

The docstring of a script (a stand-alone program) should be usable as its “usage” message, printed when the script is invoked with incorrect or missing arguments (or perhaps with a “-h” option, for “help”).



---

gliss-docopt.py
```python
"""gliss - Command Line Interface to interact with GitLab Issues.

Usage:
  gliss list
  gliss create <title> [--description=<description>] [--priority=<priority>]
  gliss show <issue-id>
  gliss close <issue-id>
  gliss comment <issue-id> <comment>
  gliss assign <issue-id> <assignee-name>

Options:
  -h --help                         Show this screen.
  -d --description=<description>    Description of the issue.
  -p --priority=<priority>          Priority of the issue.
                                    Valid values are "Low", "Medium", "High".
"""

import docopt

opts = docopt.docopt(__doc__)
print(opts)
```
---

```sh
$ python gliss-docopt.py --help     
gliss - Command Line Interface to interact with GitLab Issues.

Usage:
  gliss list
  gliss create <title> [--description=<description>] [--priority=<priority>]
  gliss show <issue-id>
  gliss close <issue-id>
  gliss comment <issue-id> <comment>
  gliss assign <issue-id> <assignee-name>

Options:
  -h --help                         Show this screen.
  -d --description=<description>    Description of the issue.
  -p --priority=<priority>          Priority of the issue.
                                    Valid values are "Low", "Medium", "High".
```

---

- approche UI-first
- plus de limite 
- le projet n'est plus maintenu depuis 2014
- il existe un fork par jazzband

---

# Le favori des bookmakers: **click**

- 13.6k ⭐
- Used by: 1M repos
- créé par Armin Ronacher (Flask, Jinja, ..)

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

---

# L'outsider: **fire**

- 24.2k ⭐
- Used by: 18k repos
- porté par google

---

gliss-fire.py
```python
import fire

class Gliss(object):
    """Command Line Interface to interact with GitLab Issues."""

    def list(self):
        """List all issues."""
        print("Listing all issues.")

    def create(self, title, description=None, priority=None):
        """Create a new issue."""
        print(f"Creating issue: {title}")
        if description:
            print(f"Description: {description}")
        if priority:
            print(f"Priority: {priority}")

    (...)

if __name__ == '__main__':
    fire.Fire(Gliss)
```
---

```sh
$ python gliss-fire.py 
NAME
    gliss-fire.py - Command Line Interface to interact with GitLab Issues.

SYNOPSIS
    gliss-fire.py COMMAND

DESCRIPTION
    Command Line Interface to interact with GitLab Issues.

COMMANDS
    COMMAND is one of the following:

     assign
       Assign an issue to an assignee.

     close
       Close an issue.

     comment
       Comment on an issue.

     create
       Create a new issue.

     list
       List all issues.
```
---

```sh
$ python gliss-fire.py create --help
NAME
    gliss-fire.py create - Create a new issue.

SYNOPSIS
    gliss-fire.py create TITLE <flags>

DESCRIPTION
    Create a new issue.

POSITIONAL ARGUMENTS
    TITLE

FLAGS
    -d, --description=DESCRIPTION
        Type: Optional[]
        Default: None
    -p, --priority=PRIORITY
        Type: Optional[]
        Default: None

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```
---

- http://xion.io/post/programming/python-dont-use-click.html
- https://click.palletsprojects.com/en/8.1.x/why/

