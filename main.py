def main():
    tasks = []
    MENU = (
        "\nWelcome to Aero Task List:\n"
        "  1. View Task List\n"
        "  2. Add Task\n"
        "  3. Delete Task\n"
        "  0. Quit\n"
    )
    
    while True:
        print(MENU)
        user_input = input("Selection #: ").strip()
        
        if user_input == "1":
            view_tasks(tasks)
        elif user_input == "2":
            task = input("Describe the task to add: ").strip()
            if task:
                tasks.append(task)
        elif user_input == "3":
            view_tasks(tasks)
            if tasks:
                try:
                    idx = int(input("\nEnter Number of task to remove: "))
                    tasks.pop(idx - 1)
                except (ValueError, IndexError):
                    print("Invalid Selection")
        elif user_input == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid Selection")

            
            
def view_tasks(tasks):
    if not tasks:
        print("No Tasks Left, Congrats!\n")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}: {task}")

    

if __name__ == "__main__":
    main()
