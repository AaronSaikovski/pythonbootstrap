<div align="center">

# Python Starter Project Boilerplate Template - v1.1.0

A Python boilerplate starter project template to setup a baseline Python project for you to get started.

[![Build Status](https://github.com/AaronSaikovski/pystarter/workflows/build/badge.svg)](https://github.com/AaronSaikovski/pystarter/actions)
[![Licence](https://img.shields.io/github/license/AaronSaikovski/pystarter)](LICENSE)

</div>
Python projects are tricky to setup correctly and as such the creation of this project came about. I hope you enjoy this and enjoy using it as much as I do.
This has been recently updated to use the awesome [Poetry](https://python-poetry.org/) packaging and dependency toolchain.

## Usage

Click the [Use this template](https://github.com/AaronSaikovski/pystarter/generate) button at the top of this project's GitHub page to get started.

## Software Requirements:

- Python v3.10 or higher needs to be installed - https://www.python.org/
- Poetry v1.5.1 or higher needs to be installed - https://python-poetry.org/docs/#installation
- - [Taskfile](https://taskfile.dev/) to run the build chain commands listed below.

## Installation:

The toolchain is driven by using [Taskfile](https://taskfile.dev/) and all commands are managed via the file `Taskfile.yml`

The list of commands is as follows:

```bash
* activate:        Activates the virtual environment.
* clean:           Cleans the environment, Overwrites the pyproject.toml file
* create:          Inits the poetry virtual environment and installs baseline packages.
* deps:            Install the dependencies.
* install:         installs the poetry environment with dependencies.
* lint:            Lints the project using ruff --fix
* release:         uses pyinstaller to package your Python application into a single package
* run:             Run the script main.py
* test:            Tests the project.
* update:          updates dependency versions
* vulncheck:       Checks for vulnerabilities in the project
```

Execute using the taskfile utility:

```bash
task <command_from_above_list>
```

To get started type,

- `task create` - to create a poetry virtual environment.
- `task deps` - to fetch and update all dependencies.
- `task activate` - to activate the virtual environment.
- `task build` - to build debug version for your target environment architecture.
- `task release` - Builds a release version for your target environment architecture - outputs to /bin folder.

## Attribution

- Advanced poetry setup: https://testdriven.io/blog/python-project-workflow/
- original concept derived from here: https://github.com/Justintime50/python-template
