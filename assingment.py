def display_menu():
    """Displays the menu options to the user."""
    print("\n" + "=" * 30)
    print("      TO-DO LIST MANAGER      ")
    print("=" * 30)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")
    print("=" * 30)


def view_tasks(todo_list):
    """Displays all tasks currently in the list."""
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYOUR TASKS:")
        for index, task in enumerate(todo_list, start=1):
            # String formatting to present the tasks neatly
            print(f"{index}. {task.capitalize()}")


def add_task(todo_list):
    """Prompts user to add a new task."""
    task = input("\nEnter the task to add: ").strip()
    if task:
        todo_list.append(task)
        print(f"Task '{task.capitalize()}' added successfully.")
    else:
        print("Task cannot be empty!")


def remove_task(todo_list):
    """Removes a task by its list number."""
    if not todo_list:
        print("\nYour to-do list is empty! Nothing to remove.")
        return

    view_tasks(todo_list)
    try:
        task_num = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task.capitalize()}' removed successfully.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")


def clear_tasks(todo_list):
    """Clears all tasks after user confirmation."""
    if not todo_list:
        print("\nYour to-do list is already empty.")
        return

    confirm = input("Are you sure you want to delete all tasks? (y/n): ").strip().lower()
    if confirm == 'y':
        todo_list.clear()
        print("All tasks cleared!")
    else:
        print("Action cancelled.")


def main():
    """Main program execution loop."""
    todo_list = []  # Initialize empty list to store tasks

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            view_tasks(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            clear_tasks(todo_list)
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()
