---
layout: image-right
image: https://media.gettyimages.com/id/79039976/fr/photo/sport-boxing-tommy-farr-the-former-british-and-empire-heavyweight-champion-in-training-for-his.jpg?s=612x612&w=0&k=20&c=-Jnzijv7PNRHkIZ02UE4Xbpxs4co359UNVqwqWEa3z8=
---

# Le vétéran du circuit : **argparse**

- inclus dans la librairie standard depuis python 2.7
- recommandé dans la documentation python (vs [getopt](https://docs.python.org/3/library/getopt.html#module-getopt) et [optparse](https://docs.python.org/3/library/optparse.html))

---
title: argparse
layout: center
---

gliss-argparse.py
```python {1-3|7-8|10-15|14-15|18-19|all}
import argparse

parser = argparse.ArgumentParser(description='Command Line Interface to interact with GitLab Issues.')

subparsers = parser.add_subparsers(title='Commands', dest='command')

# List issues
list_parser = subparsers.add_parser('list', help='List all issues')

# Create new issue
create_parser = subparsers.add_parser('create', help='Create a new issue')
create_parser.add_argument('title', help='Title of the issue')
create_parser.add_argument('-d', '--description', help='Description of the issue')
create_parser.add_argument('-p', '--priority', choices=['Low', 'Medium', 'High'],
                          default='Low', help='Priority of the issue')

# Show issue details
show_parser = subparsers.add_parser('show', help='Show details of an issue')
show_parser.add_argument('issue_id', type=int, help='ID of the issue')

...

args = parser.parse_args()
print(vars(args))
```

---
title: argparse
layout: center
---

### génération du --help à partir des valeurs des paramètres _help_
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
title: argparse
layout: center
---

### aide détaillée pour chaque commande
```sh
$ python gliss-argparse.py create --help
usage: gliss-argparse.py create [-h] [-d DESCRIPTION] [-p {Low,Medium,High}]
                                title

positional arguments:
  title                 Title of the issue

optional arguments:
  -h, --help            show this help message and exit
  -d DESCRIPTION, --description DESCRIPTION
                        Description of the issue
  -p {Low,Medium,High}, --priority {Low,Medium,High}
                        Priority of the issue
```

---
title: argparse
layout: center
---

### valeur par défaut
```sh
$ python gliss-argparse.py create "implement create issue" 
{'command': 'create', 'title': 'implement create issue', 'description': None, 'priority': 'Low'}
```

---
title: argparse
layout: center
---
### validation des arguments
```sh
$ python gliss-argparse.py create "implement create issue" --priority=critical
usage: gliss-argparse.py create [-h] [--description DESCRIPTION] [--priority {Low,Medium,High}] title
gliss-argparse.py create: error: argument --priority: invalid choice: 'critical' (choose from 'Low', 'Medium', 'High')
```

---
title: argparse
layout: center
---
### typage
```sh
$ python gliss-argparse.py show 1234                                          
{'command': 'show', 'issue_id': 1234}
```

