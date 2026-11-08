# Game Idea Generator

A small Python desktop application that randomly generates game concepts by combining a theme, genre and visual style.

Built as a small practice project to explore Python and Tkinter desktop application development.

## Features

- Randomly generated game themes.
- Randomly generated game genres.
- Randomly generated art styles.
- Simple desktop GUI using Tkinter.
- Generate new ideas at the click of a button.

## Built With

- Python 3
- Tkinter
- Random (Python standard library)

## Running the Application

Clone the repository and navigate to the project directory.

Run:

```bash
python3 main.py
```

## Building an Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the application:

```bash
pyinstaller --onefile --windowed --name "Game Idea Generator" main.py
```

The executable will be generated in the `dist` directory.

## Purpose

A small, fun project created to practise Python fundamentals and experiment with desktop application development.