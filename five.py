import os

# File definition for persistent task storage
TODO_FILE = "todo_list.txt"

def load_tasks():
    """Loads tasks from a plain text file line by line. Returns a clean list."""
    tasks = []
    if not os.path.exists(TODO_FILE):
        return tasks
    
    try:
        with open(TODO_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    # Split the line by the pipe symbol to separate status and task title
                    parts = line.split(" | ", 1)
                    if len(parts) == 2:
                        status, task_title = parts
                        tasks.append({"title": task_title, "completed": status == "DONE"})
    except (IOError, PermissionError) as error:
        print(f"\n[Warning] Could not read file storage ({error}). Starting fresh.")
    
    return tasks

def save_tasks(tasks):
    """Saves the active task array back to the text file with human-readable formatting."""
    try:
        with open(TODO_FILE, 'w') as file:
            for task in tasks:
                status = "DONE" if task["completed"] else "TODO"
                file.write(f"{status} | {task['title']}\n")
        print("\n[Success] Task file updated securely.")
    except Exception as error:
        print(f"\n[Error] Failed to write changes to task file: {error}")

def add_task(tasks):
    """Appends a new incomplete task entry to the list database."""
    print("\n--- Create New Task ---")
    task_title = input("Enter the task description: ").strip()
    
    if not task_title:
        print("[Abort] Task text cannot be empty.")
        return

    tasks.append({"title": task_title, "completed": False})
    save_tasks(tasks)
    print(f"[Success] Task added: \"{task_title}\"")

def view_tasks(tasks):
    """Displays all current tasks with clean visual checkboxes."""
    if not tasks:
        print("\n[Notice] Your To-Do list is completely empty!")
        return

    print("\n================ ACTIVE TO-DO LIST ================")
    for index, task in enumerate(tasks, 1):
        checkbox = "[✓]" if task["completed"] else "[ ]"
        print(f"{index}. {checkbox} {task['title']}")
    print("===================================================")

def complete_task(tasks):
    """Marks a selected task item index from the tracking index as DONE."""
    print("\n--- Mark Task Complete ---")
    view_tasks(tasks)
    
    if not tasks:
        return

    try:
        choice = int(input("\nEnter the number of the task to complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print(f"\n[Success] Task {choice} marked as complete!")
        else:
            print("[Error] Number out of bounds. Choice unrecognized.")
    except ValueError:
        print("[Error] Invalid input format. Please enter a valid number.")

def delete_task(tasks):
    """Permanently removes a task item from the list tracking data structures."""
    print("\n--- Delete Task Entry ---")
    view_tasks(tasks)
    
    if not tasks:
        return

    try:
        choice = int(input("\nEnter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"\n[Success] Removed: \"{removed['title']}\"")
        else:
            print("[Error] Number out of bounds. Choice unrecognized.")
    except ValueError:
        print("[Error] Invalid input format. Please enter a valid number.")

def main():
    """Main workflow environment coordinating system selection options."""
    task_list = load_tasks()

    while True:
        print("\n====== TO-DO APPLICATION INTERFACE ======")
        print("1. View Current Tasks")
        print("2. Add New Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task Record")
        print("5. Terminate Application")
        print("=========================================")
        
        choice = input("Select application command (1-5): ").strip()

        if choice == '1': view_tasks(task_list)
        elif choice == '2': add_task(task_list)
        elif choice == '3': complete_task(task_list)
        elif choice == '4': delete_task(task_list)
        elif choice == '5':
            print("\nShutting down To-Do workspace panel. Goodbye!")
            break
        else:
            print("\n[Invalid] Select from numerical commands bounds (1-5) only.")

if __name__ == "__main__":
    main()
