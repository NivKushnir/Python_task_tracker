from Task_C import Task
from datetime import datetime
import Validation as V

#The function will return datetime object of due_date
def get_due_date(task):
    return datetime.strptime(task.due_date,"%Y-%m-%d").date()


#The function will check if a task is overdue
def is_overdue(task):
    today = datetime.now().date()
    d_date = get_due_date(task)
    return d_date < today and not task.completed

#The function will check if a task is for today
def is_due_today(task):
    today = datetime.now().date()
    d_date = get_due_date(task)
    return d_date == today and not task.completed

#The function will check if the task is for this week
def is_due_this_week(task):
    today = datetime.now().date()
    d_date = get_due_date(task)
    return not task.completed and 0<(d_date-today).days <=7

#The function will return a list with all the tasks which are overdue
def get_overdue_tasks(tasks):
    return [task for task in tasks if is_overdue(task)]

#The function will return a list with all the task which are for today
def get_due_today_tasks(tasks):
    return [task for task in tasks if is_due_today(task)]

#The function will return a list with all the task which are for this week
def get_due_this_week_tasks(tasks):
    return [task for task in tasks if is_due_this_week(task)]

#The function will return a list of all the tasks which are completed
def get_completed_tasks(tasks):
    return [task for task in tasks if task.completed]

#The function will return a list of all the tasks which are not completed
def get_not_completed_tasks(tasks):
    return [task for task in tasks if not task.completed]

#The function will sort out tasks list
def sort_tasks(tasks):
       tasks.sort(key=lambda task: (task.completed,task.due_date))

#The function will return the amount of the wanted priority tasks
def count_priority(tasks,priority):
    return sum(task.priority == priority and not task.completed for task in tasks)

#The function will print the completion rate of all the user tasks
def get_completion_rate(tasks):
    if len(tasks):
        return (len(get_completed_tasks(tasks))/len(tasks))*100
    return 0

#The function will print the longest overdue task
def show_overdue_task(tasks):
    overdue_tasks = get_overdue_tasks(tasks)
    if overdue_tasks:
        print(f'The longest overdue task is:')
        show_tasks([min(overdue_tasks,key = lambda t:t.due_date)])
        print("\n")

#The function will print the closest task of this week
def show_closest_task(tasks):
    this_week_tasks =get_due_this_week_tasks(tasks)
    if this_week_tasks:
        print(f'The closest task is:')
        show_tasks([min(this_week_tasks,key = lambda t:t.due_date)])
        print("\n")

#the fuction will create a task object and will add it to the task list
def add_task(tasks):
    new_task = input("What task would you like to add: ")
    priority = V.get_valid_priority()
    d_date = V.get_valid_date()

    tasks.append(Task(new_task,False,priority,d_date))
    sort_tasks(tasks)

#the function will show all the task in the list
def show_tasks(tasks):
    if not tasks:
        print("The task list is empty")
        return
    today = datetime.now().date()
    for t in tasks:
        d_date = get_due_date(t)
        if t.completed:
            print(f'[X] {t.title} ({t.priority}) - Due date {t.due_date} {(d_date-today).days} days left')
        elif is_overdue(t):
            print(f'[ ] {t.title} ({t.priority}) - Due date {t.due_date} !!!Overdue!!! by {(today-d_date).days} days ')
        else: print(f'[ ] {t.title} ({t.priority}) - Due date {t.due_date} {(d_date-today).days} days left')

#the function will change task.completed to true
def task_complete(tasks):
    if not tasks:
        print("No tasks available")
        return
    index = V.get_valid_index(tasks,"What task number did you complete: ")-1
    tasks[index].completed = True
    sort_tasks(tasks)


#the function will show the user task statistics
def show_statistics(tasks):
    total_tasks = len(tasks)
    total_completed = sum(task.completed for task in tasks)
    print(f'Total tasks {total_tasks}')
    print(f'You completed {total_completed} tasks')
    print(f'You have {total_tasks-total_completed} remaining tasks')
    completion_rate = get_completion_rate(tasks)
    print(f'Your completion rate is : {completion_rate:.1f}%')


    print(f'High task remaining: {count_priority(tasks,"High")}')
    print(f'Medium task remaining: {count_priority(tasks,"Medium")}')
    print(f'Low task remaining: {count_priority(tasks,"Low")}')

    overdue_tasks= get_overdue_tasks(tasks)
    due_today= get_due_today_tasks(tasks)
    tasks_this_week=get_due_this_week_tasks(tasks)
    print(f'Overdue tasks {len(overdue_tasks)} \n')
    show_tasks(overdue_tasks)
    print("\n")
    print(f'Due today : {len(due_today)} tasks \n')
    show_tasks(due_today)
    print("\n")
    print(f'Due this week: {len(tasks_this_week)} tasks \n')
    show_tasks(tasks_this_week)
    print("\n")
    show_overdue_task(tasks)
    show_closest_task(tasks)


#the function will ask the user how he would like to filter the task list and will filter it accordingly 
def filter_tasks(tasks):
    filter_menu = {1:"Completed",2:"Incomplete",3:"High priority",4:"Medium priority",5:"Low priority",6:"Overdue",7:"due today",8:"due this week"}
    print(f'Here is the filter options {filter_menu}')
    filter_choice = input("What would you like to filter: ")
    while filter_choice not in ["1","2","3","4","5","6","7","8"]: 
        print("Invalid choice try again")
        print(f'Here is the filter options {filter_menu}')
        filter_choice = input("What would you like to filter: ")
        
    if filter_choice == "1":
        return get_completed_tasks(tasks)
    
    elif filter_choice == "2":
        return get_not_completed_tasks(tasks)
    
    elif filter_choice == "3":
        return [task for task in tasks if task.priority == "High"]
    
    elif filter_choice == "4":
        return [task for task in tasks if task.priority == "Medium"]
    
    elif filter_choice == "5":
        return [task for task in tasks if task.priority == "Low"]
    
    elif filter_choice == "6":
        return get_overdue_tasks(tasks)#overdue_tasks_list
    
    elif filter_choice == "7":
        return get_due_today_tasks(tasks)#due_today_list
    
    elif filter_choice =="8":
        return get_due_this_week_tasks(tasks)#tasks_this_week_list
    
#The function will allow the user to edit is tasks
def edit_task(tasks):
    for i, t in enumerate(tasks,start=1):
        print(i, t.title)
    while True :
            index = V.get_valid_index(tasks,"Which task would you like to edit: ")
            while True:
                print("1: Edit title, 2: Edit priority, 3: Edit due date, 0: Done")
                try: 
                    edit = int(input("What would you like to edit:"))
                except ValueError:
                    print("Invalid input")
                    continue
                if not 0<=edit<=3:
                    print("Invalid choice")
                    continue

                elif edit == 0:
                    break

                elif edit == 1:
                        print(f'Current title: {tasks[index-1].title}')
                        tasks[index-1].title = input("Change title to: ")
                        
                elif edit == 2:
                    print(f'Current priority: {tasks[index-1].priority}')
                    tasks[index-1].priority = V.get_valid_priority()
                    
                elif edit ==3:
                    print(f'Current due date {tasks[index-1].due_date}')
                    tasks[index-1].due_date = V.get_valid_date()
                print("\n")

            break
    sort_tasks(tasks)
    print("Task changed successfully")           

#The function will allow the user to delete his tasks
def delete_tasks(tasks):
    for i, t in enumerate(tasks,start=1):
        print(i, t.title)
    while(True):
        index = V.get_valid_index(tasks,"Which task would you like to delete ,to finish please press 0: ",True)
        if index == 0:
            break
        else:
            d_task = tasks.pop(index-1)
            print(f'{d_task.title} deleted successfully')    
    sort_tasks(tasks)    
