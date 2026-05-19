import Task as T
import Storage as S
from Task_C import Task

Menu = {1: "Add Task",2:"View Tasks",3:"Task completed", 4:"Exit"}
data = S.load_tasks()
tasks = [Task.from_dict(task_data) for task_data in data]
print(Menu)
choice = input("What would you like to do: ")
while(choice!="4"):
    if choice == "1":
        T.add_task(tasks)
        print("Task added")
    elif choice == "2":
        T.show_tasks(tasks)
    elif choice == "3":
        flag = T.task_complete(tasks)
        while(flag):
              print("Not a number, Please try again")
              T.task_complete(tasks)
        print("Task removed")
    else: print("Not a valid choice, try again")
    print(Menu)
    choice = input("What would you like to do: ")

new_data = [task.to_dict() for task in tasks]
S.save_tasks(tasks=new_data)
print("Have a good day")