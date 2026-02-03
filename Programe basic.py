def show_menu():
    print("\n--- Task Tracker ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Show progress")
    print("5. Exit")


tasks = []


def add_task():
    name = input("Enter task name: ")
    tasks.append({"name": name, "done": False})
    print("Task added")


def view_tasks():
    if not tasks:
        print("No tasks added yet.")
        return

    index = 1
    for task in tasks:
        if task["done"]:
            status = "✓"
        else:
            status = "✗"

        print(f"{index}. {task['name']} [{status}]")
        index += 1


def task_complete():
    task_number = int(input("Choose task number: "))
    index = task_number - 1

    if index < 0 or index >= len(tasks):
        print("Incorrect task number")
    else:
        tasks[index]["done"] = True
        print("Task completed")


while True:
    show_menu()
    choice = int('Choose an option:')

    if not choice.isdigit():
        print("Please enter a number.")
        continue

    choice = int(choice)
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        task_complete()
    elif choice == 4:
        print('Task in progress')
    elif choice == 5:
        print('Thanks for all the fish!')
        break
    else:
        print('Invalid choice')
