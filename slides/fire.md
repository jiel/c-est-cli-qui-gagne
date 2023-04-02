---
layout: image-right
image: https://media.gettyimages.com/id/535582502/fr/photo/gagnant-boxeur-enfant-soulevant-ses-mains-avec-la-victoire.jpg?s=612x612&w=0&k=20&c=Lv_Yq-6H6YZhqbYDl3OfV1e5rTLFN_8FDd4ixM6dKHU=
---

# L'outsider : **fire**

- 24.2k ⭐
- Used by: 18k repos
- porté par google

---
title: fire
layout: center
---

gliss-fire.py
```python
from fire import Fire

class Gliss:
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
    Fire(Gliss)
```

---
title: fire
layout: center
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
title: fire
layout: center
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