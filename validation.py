from datetime import datetime

def validate_task_title(title):
    while not title.strip():
        print("Title cannot be empty.")
        title = input("Enter a valid title: ")
    return title
    
def validate_task_description(description):
    while not description.strip():
        print("Description cannot be empty.")
        description = input("enter a vadid description: ")
    
def validate_due_date(due_date):
    while True:
        try:
            formatted = datetime.strptime(due_date, "%Y-%m-%d").date()
            return formatted
        except ValueError:
            print("Invalid date formate. Use YYYY-MM-DD.")
            due_date = input("Enter a valid due date: ")