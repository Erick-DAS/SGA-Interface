# SGA-Interface

## Snake Game Arcade Project

This repository is part of Snake Game Arcade (S.G.A) project development from subject "Laboratório Digital I" (PCS3635), wich is a subject from POLI-USP that aims at developing F.P.G.A projects wich integrate with different software/firmware components.

It contains the code of the interface that shows the game screens. To execute it, run `interface/snake-game.py` file.

Members of the group:

- Erick Diogo de Almeida Sousa 
- Carlos Maria Engler Pinto  
- João Pedro Bassetti Freitas

Teacher
- Edson Toshimi Midorikawa

## Setup

Main dependencies:
- Poetry
- Python 3.10 or higher

Your Python version needes to be at least 3.10 in order to use statements such as `match - case`. Prefferebly use [pyenv](https://github.com/pyenv/pyenv), the repo has a `.python-version` for that.

This project uses [poetry](https://python-poetry.org/) for dependency management. Follow the steps below in order to install and use all the dependencies:

1. Install `poetry` on your machine if you still don't have it with `pip` or prefferebly `pipx`. Follow the [docs](https://python-poetry.org/docs/)
2. Clone the project
3. At root, run `poetry shell` in order to start the virtual environment
4. Run `poetry install` to install the dependencies. All of them are listed at `pyproject.toml`
5. Run the files manually with `python`