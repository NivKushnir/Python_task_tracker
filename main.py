import Task as T
import Storage as S
from Task_C import Task

#The trackers menu
Menu = {1: "Add Task",2:"View Tasks",3:"Task completed", 4:"Show Statistics",5:"Filter Tasks" ,0:"Exit"}
tasks = S.load_tasks() # loadind the json file to a list
print(Menu)
choice = input("What would you like to do: ") #getting an input of what the user would like to do
while(choice!="0"):
    if choice == "1":#adding a task
        T.add_task(tasks)
        print("Task added")
    elif choice == "2":#show all the tasks
        T.show_tasks(tasks)
    elif choice == "3":#the user completed a task and updating it 
        flag = T.task_complete(tasks)
        while(flag):
              print("Not a number, Please try again")
              T.task_complete(tasks)
        print("Task completed")
    elif choice == "4": #shows all the statistics of the user tasks 
        print("Your statistics: \n")
        T.show_statistics(tasks)
    elif choice == "5": # the user will filter what tasks he would like to see
        filtered_tasks = T.filter_tasks(tasks)
        T.show_tasks(filtered_tasks)
    else: print("Not a vaild option")
    print(Menu)
    choice = input("What would you like to do: ")

#saves the tasks list to a json file
S.save_tasks(tasks=tasks)
print("Have a good day")