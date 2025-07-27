tasks = []

def add_task():
    task = input("Enter a new task")
    tasks.append(task)
    print("Task added!")


def view_tasks():
    if not tasks:
        print("No tasks yet")

    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}.{task}")

def menu():
    while True:
        print("\n ---TO-DO LIST MENU---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("GoodBye")
            break
        else:
            print("Invalid option. Try again")

menu()
