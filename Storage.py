import json
def save_tasks(tasks):
    with open("tasks_list","w") as file:
        json.dump(tasks, file,indent=4)
    print("Tasks saved")

def load_tasks():
    try:
        with open("task_list","r") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []
