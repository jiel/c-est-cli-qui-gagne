---
layout: image-right
image: https://media.gettyimages.com/id/498188417/fr/photo/boxer-with-arms-raised.jpg?s=612x612&w=0&k=20&c=8OUdUcJGeejv3pZsuvj6H1_eR_3OBGkrRUyxTrIiJ1o=
---

# L'ancienne gloire : **docopt**

<v-clicks>

- proposé à pycon UK 2012 http://youtu.be/pXhcPJK5cMc
- 7.8k ⭐ 
- Used by: 86k repos
- approche recommandée par la [PEP 257](https://peps.python.org/pep-0257/)

</v-clicks>

<v-click>

> _The docstring of a script (a stand-alone program) should be usable as its “usage” message, printed when the script is invoked with incorrect or missing arguments (or perhaps with a “-h” option, for “help”)._

</v-click>

---
title: docopt
layout: center
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
title: docopt
layout: center
---

### Tout le --help mais rien d'autre que le --help

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
  -p --priority=<priority>          Priority of the issue [default: Low].
                                    Valid values are "Low", "Medium", "High".
```

---
title: docopt
layout: center
---

### [default: Low] est supporté
```sh
python gliss-docopt.py create "implement create issue"
{'--description': None,
 '--priority': 'Low',
 '<assignee-name>': None,
 '<comment>': None,
 '<issue-id>': None,
 '<title>': 'implement create issue',
 'assign': False,
 'close': False,
 'comment': False,
 'create': True,
 'list': False,
 'show': False}
```

---
title: docopt
layout: center
---

### mais pas de validation des valeurs
```sh
$ python gliss-docopt.py create toto --priority critical
{'--description': None,
 '--priority': 'critical',
 '<assignee-name>': None,
 '<comment>': None,
 '<issue-id>': None,
 '<title>': 'toto',
 'assign': False,
 'close': False,
 'comment': False,
 'create': True,
 'list': False,
 'show': False}
```
---
title: docopt
layout: center
---

### pas d'aide spécifique aux commandes
```sh
python gliss-docopt.py create --help
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
  -p --priority=<priority>          Priority of the issue [default: Low].
                                    Valid values are "Low", "Medium", "High".
```

---
title: docopt
layout: center
---

### ca va doc ?
<v-clicks>

- porté dans 23 langages
- le projet n'est plus maintenu depuis 2014 😢
- il existe un fork par la [communauté jazzband](https://jazzband.co/) : [docopt-ng](https://github.com/jazzband/docopt-ng)

</v-clicks>