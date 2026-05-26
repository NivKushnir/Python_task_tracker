from Task_C import Task
from datetime import datetime

#the fuction will create a task object and will add it to the task list
def add_task(tasks):
    new_task = input("What task would you like to add: ")
    p = input("What is the task priority: High/Medium/Low: ")
    while p not in ["High","Medium","Low"]:
        p = input("What is the task priority: High/Medium/Low")
    
    valid = False
    while not valid:
        d_date = input("What is the due date of the task: YYYY-MM-DD ")
        try:
            datetime.strptime(d_date,"%Y-%m-%d")
            valid = True
        except ValueError:
            print("Invalid due date, try again!")

    tasks.append(Task(new_task,False,p,d_date))
    tasks.sort(key=lambda task: (task.completed,task.due_date))

#the function will show all the task in the list
def show_tasks(tasks):
    if not tasks:
        print("The task list is empty")
        return
    today = datetime.now()
    for t in tasks:
        d_date = datetime.strptime(t.due_date,"%Y-%m-%d")
        if t.completed:
            print(f'[X] {t.title} ({t.priority}) - Due date {t.due_date} {(d_date-today).days} days left')
        elif d_date.date() < today.date() and not t.completed:
            print(f'[ ] {t.title} ({t.priority}) - Due date {t.due_date} !!!Overdue!!! by {(today-d_date).days} days ')
        else: print(f'[ ] {t.title} ({t.priority}) - Due date {t.due_date} {(d_date-today).days} days left')

#the function will change task.completed to true
def task_complete(tasks):
    if not tasks:
        print("No tasks available")
        return
    try:
        index = int(input("What task number did you complete: "))-1
        if 0<= index < len(tasks):
            tasks[index].completed = True
            tasks.sort(key=lambda task: (task.completed,task.due_date))
    except ValueError:
        return True

#the function will show the user task statistics
def show_statistics(tasks):
    total_tasks = len(tasks)
    total_completed = sum(task.completed for task in tasks)
    print(f'Total tasks {total_tasks}')
    print(f'You completed {total_completed} tasks')
    print(f'You have {total_tasks-total_completed} remaining tasks')
    if total_tasks:
        print(f'Completion rate {(total_completed/total_tasks)*100:.1f}%')
    else: print("Comletion rate 0%")

    total_High = sum(task.priority == "High" and not task.completed for task in tasks)
    total_Medium = sum(task.priority == "Medium" and not task.completed for task in tasks)
    total_Low = sum(task.priority == "Low" and not task.completed for task in tasks)
    print(f'High task remaining: {total_High}')
    print(f'Medium task remaining: {total_Medium}')
    print(f'Low task remaining: {total_Low}')

    overdue_tasks=0
    overdue_tasks_list = []
    due_today=0
    due_today_list =[]
    tasks_this_week=0
    tasks_this_week_list=[]
    today = datetime.now()
    for t in tasks:
        d_date = datetime.strptime(t.due_date,"%Y-%m-%d")
        if d_date.date() < today.date() and not t.completed:
            overdue_tasks+=1
            overdue_tasks_list.append(t)
        elif d_date.date() == today.date() and not t.completed:
            due_today+=1
            due_today_list.append(t)
        elif not t.completed and 0<(d_date-today).days <=7:
            tasks_this_week+=1
            tasks_this_week_list.append(t)
    print(f'Overdue tasks {overdue_tasks} \n')
    show_tasks(overdue_tasks_list)
    print("\n")
    print(f'Due today : {due_today} tasks \n')
    show_tasks(due_today_list)
    print("\n")
    print(f'Due this week: {tasks_this_week} tasks \n')
    show_tasks(tasks_this_week_list)
    print("\n")
    if overdue_tasks_list:
        print(f'The longest overdue task is:')
        show_tasks([min(overdue_tasks_list,key = lambda t:t.due_date)])
        print("\n")
    if tasks_this_week_list:
        print("The closest task is:")
        show_tasks([min(tasks_this_week_list,key = lambda t:t.due_date)])
        print("\n")



    #added time statistics - תוסיף אחר כך בgit

#the function will ask the user how he would like to filter the task list and will filter it accordingly 
def filter_tasks(tasks):
    filter_menu = {1:"Completed",2:"Incomplete",3:"High priority",4:"Medium priority",5:"Low priority"}
    print(f'Here is the filter options {filter_menu}')
    filter_choice = input("What would you like to filter: ")
    filtered_tasks =[]
    while filter_choice not in ["1","2","3","4","5"]: 
        print("Invalid choice try again")
        print(f'Here is the filter options {filter_menu}')
        filter_choice = input("What would you like to filter: ")
    if filter_choice == "1":
        for task in tasks:
            if task.completed:
                filtered_tasks.append(task)
        return filtered_tasks
    elif filter_choice == "2":
        for task in tasks:
            if not task.completed:
                filtered_tasks.append(task)
        return filtered_tasks
    elif filter_choice == "3":
        for task in tasks:
            if task.priority == "High":
                filtered_tasks.append(task)
        return filtered_tasks
    elif filter_choice == "4":
        for task in tasks:
            if task.priority == "Medium":
                filtered_tasks.append(task)
        return filtered_tasks
    elif filter_choice == "5":
        for task in tasks:
            if task.priority == "Low":
                filtered_tasks.append(task)
        return filtered_tasks