# Personal Task Tracker 

A desktop task management application built with Python and Tkinter.

The application helps users organize tasks, track deadlines, monitor progress, and manage priorities through a graphical user interface.
**Status:** Completed personal project for learning Python, GUI development, data persistence, and software design principles.

## Project Status

Current Version: v1.0

Completed personal learning project focused on Python, GUI development, SQLite integration, and software engineering fundamentals.

The SQLite database file (tasks.db) is excluded from version control and will be created automatically on first run.

## Why I Built This Project

I built this project as a personal learning exercise to gain hands-on experience with Python application development, graphical user interfaces, database integration, and software engineering best practices.
---

## Features

### Task Management

* Add new tasks
* Edit existing tasks
* Delete tasks
* Mark tasks as completed

### Organization

* Priority levels (High / Medium / Low)
* Categories:

  * Study
  * Work
  * Personal
  * Health
  * Programming

### Search & Filtering

* Search by title
* Search by priority
* Search by date range
* Filter tasks
* Sort tasks by:

  * Due date
  * Priority
  * Title
  * Category

### Statistics

* Completion rate
* Tasks completed
* Tasks remaining
* Priority statistics
* Category statistics
* Overdue tasks
* Due today
* Due this week
* Closest upcoming task

### Additional Features

* Automatic SQLite save/load
* CSV export
* Overdue task notifications
* Color-coded task display

### Data Persistence

* SQLite database storage
* Automatic database creation
* Automatic data loading on startup
* Automatic data saving on changes

---

## Technologies

* Python
* Tkinter
* ttk
* CSV
* Git
* SQLite

---

## Screenshots

### Main Window

![Main Window](images/main_window.png)

### Statistics Window

![Statistics](images/statistics_window.png)

### Search Window

![Search](images/search_window.png)

### Demo
![Demo](images/demo.gif)

---

## Project Structure

```text
main.py          - Application entry point
gui.py           - Graphical user interface
Task.py          - Task operations
Task_C.py        - Task class definition
Storage.py       - Save and load operations
Validation.py    - Input validation
Database.py      - SQLite SQLite CRUD operations
```

---

## How to Run

```bash
python main.py
```
## Installation

```bash
git clone <repository-url>
cd Personal-Task-Tracker
pip install -r requirements.txt

---

## Future Improvements

* Treeview-based task table
* Graphical charts and dashboard
* Dark mode
* Scheduled reminders
* Unit tests
* Executable application build


## What I Learned

This project helped me practice and strengthen skills in:

* Object-Oriented Programming (OOP)
* GUI development with Tkinter
* SQLite database design and CRUD operations
* Data persistence and file handling
* Git branching, merging, and version control workflows
* Input validation and error handling
* Software modularization and code organization
* Packaging Python applications with PyInstaller
* Debugging and troubleshooting real-world issues
