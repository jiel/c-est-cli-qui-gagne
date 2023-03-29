---
layout: image-right
image: https://media.gettyimages.com/id/498188417/fr/photo/boxer-with-arms-raised.jpg?s=612x612&w=0&k=20&c=8OUdUcJGeejv3pZsuvj6H1_eR_3OBGkrRUyxTrIiJ1o=
---

# L'ancienne gloire : **docopt**

- 7.8k ⭐ 
- Used by: 86k repos
- proposé à pycon UK 2012 http://youtu.be/pXhcPJK5cMc
- porté dans 23 langages
- approche recommandée par la [PEP 257](https://peps.python.org/pep-0257/)

The docstring of a script (a stand-alone program) should be usable as its “usage” message, printed when the script is invoked with incorrect or missing arguments (or perhaps with a “-h” option, for “help”).

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
title: docopt
layout: center
---

- approche UI-first
- plus de limite 
- le projet n'est plus maintenu depuis 2014
- il existe un fork par jazzband
