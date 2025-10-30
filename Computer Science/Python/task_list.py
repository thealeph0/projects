def add_task(filename):
    """Append a new task to the file."""
    task = input("Enter task name: ")
    
    with open(filename, 'a') as f:
        f.write(f"0 | {task}\n")
    print(f"Task added successfully!\n")

def view_task(filename):
    """Read and display all contacts."""
    try:
        with open(filename, 'r') as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks found.\n")
                return
            print("TODO LIST:")
            for i , task in enumerate(tasks, 1):
                status, desc = task.strip().split(" | ")
                status_val = '[X]' if status == "1" else "[ ]"
                print(f"{status_val} {i}. {desc}")
            print()
    except FileNotFoundError:
        print("No tasks file found. Add some tasks first.\n")

def search_contact(filename):
    """Mark specific task as cmoplet."""
    search_name = input("Enter the name of the contact: ")
    try:
        with open(filename, 'r') as f:
            tasks = f.readlines()
        if not tasks:
            print("No tasks to mark")
            return
        view_tasks(filename) ## view tasks before marking
        num = int(input("Enter the task number you would like complete."))
        
        if num <1 or num > len(tasks):
            print("You invalid")
            return
        
                  
    except ValueError:
        print("Please enter a valid number. \n")
    except FileNotFoundError:
        print("No contacts file found. Add some contacts first.\n")

def main():
    filename = 'tasks.txt'
    while True:
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Contact")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(filename)
        elif choice == '2':
            view_tasks(filename)
        elif choice == '3':
            search_contact(filename)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()

