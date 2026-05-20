import json
import Task
from Task_C import Task

def save_tasks(tasks):
    data = [task.to_dict() for task in tasks]
    with open("tasks_list","w") as file:
        json.dump(data, file,indent=4)
    print("Tasks saved")

def load_tasks():
    try:
        with open("tasks_list","r") as file:
            data = json.load(file)
            tasks = [Task.from_dict(task_data) for task_data in data]
            return tasks
    except FileNotFoundError:
        return []
