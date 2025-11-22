from datetime import datetime

# Import validation functions
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date - validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    try:
        index = int(index) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    except ValueError:
        print("Please enter a valid number.")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    print("\nPending Tasks:")
    pending = [t for t in tasks if not t["completed"]]

    if not pending:
        print("no pending tasks!")
        return
    
    for i, tasks in enumerate(pending, start=1):
        print(f"{i}. {task['title']} (Due: {task['due_date']})")


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0
    completed = len([t for t in tasks if t["completed"]])
    progress = (completed / len(tasks)) * 100
    return progress