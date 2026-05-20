import Task as T
import Storage as S
from Task_C import Task

Menu = {1: "Add Task",2:"View Tasks",3:"Task completed", 4:"Show Statistics",5:"Filter Tasks" ,0:"Exit"}
tasks = S.load_tasks()
print(Menu)
choice = input("What would you like to do: ")
while(choice!="0"):
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
        print("Task completed")
    elif choice == "4": 
        print("Your statistics: \n")
        T.show_statistics(tasks)
    elif choice == "5":
        filtered_tasks = T.filter_tasks(tasks)
        T.show_tasks(filtered_tasks)
    else: print("Not a vaild option")
    print(Menu)
    choice = input("What would you like to do: ")

S.save_tasks(tasks=tasks)
print("Have a good day")