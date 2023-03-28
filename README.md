# Welcome to [Slidev](https://github.com/slidevjs/slidev)!

To start the slide show:

- `npm install`
- `npm run dev`
- visit http://localhost:3030

Edit the [slides.md](./slides.md) to see the changes.

Learn more about Slidev on [documentations](https://sli.dev/).

## Python gliss project

### Installation

```shell
cd gliss

# installs the expected Python version
pyenv install $(cat .python-version)

# creates the virtual environment
python -m venv .venv

# activates the environment
source .venv/bin/activate

# installs the dependencies
pip install -r requirements.txt
```

### Run the CLI implementations

```shell
# gliss-argparse implementation
# 1. help
python -m gliss-argparse --help
# 2. issue creation
python -m gliss-argparse create "write installation documentation" --description="use markdown in README.md" --priority Medium

# gliss-click implementation
# 1. help
python -m gliss-click
# 2. issue creation
python -m gliss-click create "write installation documentation" --description="use markdown in README.md" --priority Medium

# gliss-docopt implementation
# 1. help
./gliss-docopt.py
python -m gliss-docopt
# 2. issue creation
./gliss-docopt.py create "write installation documentation" --description="use markdown in README.md" --priority Medium
python -m gliss-docopt create "write installation documentation" --description="use markdown in README.md" --priority Medium

# gliss-fire implementation
# 1. help
python -m gliss-fire

# 2. issue creation
python -m gliss-fire create --title "write installation documentation" --description="use markdown in README.md" --priority Medium
python -m gliss-fire create "write installation documentation" --description="use markdown in README.md" --priority Medium
```
