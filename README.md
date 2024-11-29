# SGA-Interface

## Snake Game Arcade Project

This repository is part of Snake Game Arcade (S.G.A) project development from subjects PCS3635 - "Laboratório Digital I" ([1.0 release](https://github.com/Erick-DAS/SGA-Interface/releases/tag/v1.0.0)) and PCS3645 - "Laboratório Digital 2" (latest version), wich are subjects from POLI-USP that aim at developing F.P.G.A projects, integrating with different software/firmware components.

It contains the code of the interface that shows the game screens.

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

## Execution

### 1. Game logic

Flash your FPGA board with the main project's `.qar`, available at [this repo](https://github.com/JPBF100/LabDig2).

### 2. Connect to PC

Connect your FPGA board to the computer, utilizing a serial port to USB converter.

### 3. Adapt code to right port

In the file `interface/snake-game.py`, at the very beggining of the main function, you should change the serial port to the right port. In order to do so, follow the steps below. 

#### Ubuntu
Your port will be `/dev/ttyUSB0`.

#### Windows
Before plugging in the USB cable, open device manager.

Then, plug the USB cable and see what COM port corresponds to it, for example, `COM5`.

### 4. Run the code

Run `interface/snake-game.py` file.
