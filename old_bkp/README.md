# Hangman Game (Legacy)

This directory contains the original implementation of the Hangman game built using Python and Tkinter.

## Overview
A classic Hangman game where users guess letters to uncover a hidden word. This version includes:
- **GUI Version**: Built with `tkInter` (`hangman_app.py`).
- **Console Version**: A CLI-based version (`hangman_console_app.py`).
- **Database Integration**: Uses MySQL for storing and retrieving game data (words, etc.).
- **Configuration**: Configured via `config.ini`.

## Project Structure
- `hangman_app.py`: Main entry point for the GUI application.
- `hangman_console_app.py`: CLI version of the game.
- `draw_hangman.py`: Logic for rendering the hangman visuals.
- `insert.py`: Script to populate the MySQL database with initial data.
- `config.ini`: Database configuration file.
- `resources/`: Contains assets used by the game.
- `Hangman/`: Core logic and modules.
- `requirements.txt`: Python dependencies.

## Setup & Running
1. **Prerequisites**: Python 3, Pip, and a running MySQL server.
2. **Database**: Create a MySQL database and update `config.ini` with your credentials.
3. **Environment**: It is recommended to use a virtual environment.
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Initialize Data**:
   ```bash
   python insert.py
   ```
6. **Run**:
   - GUI: `python hangman_app.py`
   - CLI: `python hangman_console_app.py`

---
*This code was moved to `old_bkp` on 2026-04-26 to make way for new development.*
