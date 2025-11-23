from .validation import validate_task_title, validate_task_description, validate_due_date

# Global list to store all tasks
tasks = []


def add_task(title, description, due_date):
    """Validate input and add a new task to the global tasks list."""
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index):
    """
    Mark a task as complete.
    index: string or int, 1-based index into the full tasks list.
    """
    if not tasks:
        print("There are no tasks to mark as complete.")
        return

    try:
        index = int(index) - 1  # Convert to 0-based index
    except ValueError:
        print("Please enter a valid number.")
        return

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    if tasks[index]["completed"]:
        print(f"Task '{tasks[index]['title']}' is already marked as complete.")
        return

    tasks[index]["completed"] = True
    print(f"Task '{tasks[index]['title']}' marked as complete!")


def view_pending_tasks():
    """Display all tasks that are not completed."""
    print("\nPending Tasks:")

    if not tasks:
        print("No tasks have been added yet.")
        return

    # Build a list of (real_index, task) for pending tasks
    pending = [(i, t) for i, t in enumerate(tasks, start=1) if not t["completed"]]

    if not pending:
        print("No pending tasks! All tasks are complete.")
        return

    for display_num, (real_index, task) in enumerate(pending, start=1):
        # display_num = 1, 2, 3... just for the pending list view
        # real_index = Task # in the main list (used for marking complete)
        print(f"{display_num}. {task['title']} (Task #{real_index}, Due: {task['due_date']})")


def calculate_progress():
    """Return the percentage of tasks that are completed."""
    if not tasks:
        return 0.0

    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100
