import os

# Get folder where todo.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_FILE = os.path.join(BASE_DIR, "tasks.txt")

def load_tasks():
    """Load tasks from file into a list"""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks back to the file"""
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📂 No tasks found!")
    else:
        print("\n📝 To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"❌ Task removed: {removed}")
    else:
        print("⚠️ Invalid task number!")

def todo_app():
    print("=== Simple To-Do List App ===")
    while True:
        print("\nChoose option:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            try:
                num = int(input("Enter task number to remove: "))
                remove_task(num)
            except ValueError:
                print("⚠️ Please enter a valid number!")

        elif choice == "4":
            print("Exiting To-Do App. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice! Try again.")

if __name__ == "__main__":
    todo_app()
