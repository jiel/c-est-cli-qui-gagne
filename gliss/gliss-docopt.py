#!/usr/bin/env python
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
  -p --priority=<priority>          Priority of the issue [default: Low].
                                    Valid values are "Low", "Medium", "High".
"""

from docopt import docopt

if __name__ == '__main__':
  opts = docopt(__doc__)
  print(opts)