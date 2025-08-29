from modules.filehandler import save_json, load_json
import os

def main():
    path = "data/data.json"
    tasks = []
    
    while True:
        print("Welcome to Aero Task List, please read carefully as the following menu items have changed:")
        print("#1 View Task List")
        print("#2 Add Task to Task List")
        print("#3 Delete Task from Task List")
        user_input = input("Selection #: ")
        
        if user_input == "1":
            if len(tasks) == 0:
                print("\nNo Tasks Left, Congrats!\n")
            view_tasks(tasks)
        elif user_input == "2":
            tasks.append(input("\nPlease describe Task to add: "))
        elif user_input == "3":
            view_tasks(tasks)
            task_to_remove = int(input("\nEnter Number of task to remove: "))
            tasks.pop(task_to_remove - 1)
        else:
            print("\nInvalid Selection\n")
            
            
def view_tasks(tasks):
    print()
    for i in range(len(tasks)):
        print(f"{i + 1}: {tasks[i]}")

    

if __name__ == "__main__":
    main()
