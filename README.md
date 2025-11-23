# Task Management System

A simple Python-based command-line application that allows users to manage tasks, mark them as complete, view pending tasks, and track their overall progress.
This project demonstrates modular programming, input validation, and basic data structures.

## Project Structure
task_management_system/
├── main.py
└── task_manager/
    ├── __init__.py
    ├── task_utils.py
    └── validation.py


main.py – Menu-based interface for interacting with the program

task_utils.py – Functions for adding tasks, marking complete, viewing pending tasks, and calculating progress

validation.py – Input validation functions for task title, description, and due date

task_manager package – Organizes all task-related modules

## Features
### Add a task

Users can add a task with:

Title

Description

Due date (validated for correct format)

### Mark a task as complete

Users can mark any existing task (by its number) as completed.

### View pending tasks

Displays all incomplete tasks, including their due dates and their corresponding Task # in the full list.

### Track progress

Shows the percentage of tasks completed out of the total number of tasks.

## Requirements

Python 3.7+

No external libraries required

Works on macOS, Windows, and Linux

## How to Run the Program

Navigate to the project folder:

cd task_management_system


Run the main script:

python main.py


Use the on-screen menu to interact with the system.

## Example Task Dictionary

Each task is stored using this structure:

task = {
    "title": "Groceries",
    "description": "Shop at Market Basket for food",
    "due_date": "2024-06-26",
    "completed": True
}

## Modules Overview
validation.py
Contains:
- validate_task_title(title)
- validate_task_description(description)
- validate_due_date(due_date)
- Ensures user input is correct and prevents invalid task entries.

task_utils.py
- Provides core functionality:
- add_task(title, description, due_date)
- mark_task_as_complete(index)
- view_pending_tasks()
- calculate_progress()
- Stores tasks in a global tasks list used by the entire system.

main.py
- Implements a menu-driven interface that allows the user to:
- Add tasks
- Mark tasks complete
- View pending tasks
- Check progress
- Exit
- Uses functions from the task_manager package.

##📄 License

This project is created for educational purposes and may be reused or modified freely.