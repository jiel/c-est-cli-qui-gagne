---
title: command line interface
layout: center
---

# Command Line Interface

<v-clicks>

- une IHM qui remonte aux années 60 
- une IHM de choix pour du tooling IT
- avantages :
  - rapidité d'usage (mémoire musculaire)
  - composabilité (scripting)
  - simplicité de développement

</v-clicks>

---
title: cli grammar
layout: center
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

<v-clicks>

- respect des conventions (POSIX..)
- des arguments et des options logiques et intuitifs
- auto apprentissage avec l'aide intégrée

</v-clicks>

---
title: gliss
layout: center
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