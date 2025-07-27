tasks = []

def add_task():
    task_name = input("Enter a new task: ")
    task = {"task": task_name, "done":False}
    tasks.append(task)
    print("Task added!")


def view_tasks():
    if not tasks:
        print("No tasks yet")

    else:
        print("\n Your Tasks:")
        for i,t  in enumerate(tasks, 1):
            status = "\u2705" if t["done"] else "\u274C"
            print(f"{i}.{t['task']}[{status}]")

def mark_task_complete():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int (input("Enter the number of the task to mark as complete: "))
        if 1<= task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            print("Task marked as complete!")

        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try: 
        task_number = int(input("Enter the number of the task to delete: "))
        if 1<= task_number <= len(tasks):
            deleted = tasks.pop(task_number-1)
            print(f"\U0001F5D1 Task '{deleted['task']}' deleted")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def edit_task():
    view_tasks()
    if not tasks:
        return
    
    try:
        task_number = int(input("Enter the number of task to edit: "))
        if 1 <=task_number <= len(tasks):
            new_text = input("Enter the new task: ")
            tasks[task_number - 1]["tasks"] = new_text
            print("Task updated")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")


def menu():
    while True:
        print("\n ---TO-DO LIST MENU---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            print("GoodBye")
            break
        else:
            print("Invalid option. Try again")

menu()
