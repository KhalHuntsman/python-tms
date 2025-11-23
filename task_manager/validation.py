from datetime import datetime

def validate_task_title(title):
    """Ensure the title is not empty."""
    while not title.strip():
        print("Title cannot be empty.")
        title = input("Enter a valid title: ")
    return title.strip()


def validate_task_description(description):
    """Ensure the description is not empty."""
    while not description.strip():
        print("Description cannot be empty.")
        description = input("Enter a valid description: ")
    return description.strip()


def validate_due_date(due_date):
    """
    Ensure the due date is in YYYY-MM-DD format.
    Returns a string in that format.
    """
    while True:
        try:
            parsed = datetime.strptime(due_date.strip(), "%Y-%m-%d").date()
            # Store as a string in consistent format
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            due_date = input("Enter a valid due date (YYYY-MM-DD): ")
