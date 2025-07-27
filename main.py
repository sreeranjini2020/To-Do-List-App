tasks = []

# 1. Add Task
def add_task():
    task_name = input("Enter a new task: ")
    task = {"task": task_name, "done":False}
    tasks.append(task)
    print("Task added!")

# 2. View Tasks
def view_tasks():
    if not tasks:
        print("No tasks yet")

    else:
        print("\n Your Tasks:")
        for i,t  in enumerate(tasks, 1):
            status = "\u2705" if t["done"] else "\u274C"
            print(f"{i}.{t['task']}[{status}]")

# 3. Mark Task as Complete
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

# 4. Delete Task
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

# 5. Edit Task
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


# 6. Save tasks to file
def save_tasks_to_file():
    with open("task.txt", "w") as file:
        for task in tasks:
            status = "1" if task["done"] else "0"
            file.write(f"{status}|{task['task']}\n")


# 7. Load tasks from file
def load_task_from_file():
    try:
        with open("task.txt", "r") as file:
            for line in file:
                status, task_text = line.strip().split("|", 1)
                completed = True if status == "1" else False
                tasks.append({"task": task_text, "completed": completed})
    except FileExistsError:
        pass


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
            save_tasks_to_file()
            print("GoodBye")
            break
        else:
            print("Invalid option. Try again")

# 9. Entry Point
if __name__ == "__main__":
    menu()