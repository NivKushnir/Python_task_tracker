from Task_C import Task

def add_task(tasks):
    new_task = input("What task would you like to add: ")
    p = input("What is the task priority: High/Medium/Low")
    while p not in ["High","Medium","Low"]:
        p = input("What is the task priority: High/Medium/Low")
    tasks.append(Task(new_task,False,p))
    tasks.sort(key=lambda task: task.completed)

def show_tasks(tasks):
    if not tasks:
        print("The task list is empty")
        return
    for t in tasks:
        if t.completed:
            print(f'[X] {t.title} ({t.priority})')
        else: print(f'[ ] {t.title} ({t.priority})')

def task_complete(tasks):
    if not tasks:
        print("No tasks available")
        return
    try:
        index = int(input("What task number did you complete: "))-1
        if 0<= index < len(tasks):
            tasks[index].completed = True
            tasks.sort(key=lambda task: task.completed)
    except ValueError:
        return True

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