import json
import Task
from Task_C import Task
#the function will take the tasks list and will convert it to a json file
def save_tasks(tasks):
    data = [task.to_dict() for task in tasks]
    with open("tasks_list.json","w") as file:
        json.dump(data, file,indent=4)
    print("Tasks saved")
#the function will convert the json file to adictinary and then to a list
def load_tasks():
    try:
        with open("tasks_list.json","r") as file:
            data = json.load(file)
            tasks = [Task.from_dict(task_data) for task_data in data]
            return tasks
    except FileNotFoundError:
        return []
