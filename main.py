from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
)

def main():
    """give and define choices, 
    if elif else statements to define what happens under a choice
    call functions as needed 
    handles inputs and erorrs"""
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)

        elif choice == "2":
            index = input("Enter the task number to mark complete (Task #): ")
            mark_task_as_complete(index)

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            progress = calculate_progress()
            print(f"Progress: {progress:.2f}% of tasks completed.")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
