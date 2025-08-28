from modules.task import Task
from modules.filehandler import save_json, load_json
import json

def main():
    task = Task()
    print(task)
    
    data = load_json()
    
    print(data)

    

if __name__ == "__main__":
    main()
