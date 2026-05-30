from datetime import datetime

#The function will verify the priority the user will input
def get_valid_priority():
    while True:
        p = input("What is the task priority: High/Medium/Low: ").strip().capitalize()

        if p in ["High", "Medium", "Low"]:
            return p

        print("Invalid priority")

#The function will verify the due date the user will input
def get_valid_date():
    valid = False
    while not valid:
        d_date = input("What is the due date of the task: YYYY-MM-DD ")
        try:
            datetime.strptime(d_date,"%Y-%m-%d")
            valid = True
        except ValueError:
            print("Invalid due date, try again!")
    return d_date

#The function will verify the index the user will input
def get_valid_index(tasks,messge,allow_zero=False):
    while True :
        try:
            index = int(input(messge))
        except ValueError:
            print("Invalid input")
            continue

        if index == 0 and allow_zero:
            return 0
        
        if not 1<=index<=len(tasks):
            print("Invalid index")
            continue

        return index