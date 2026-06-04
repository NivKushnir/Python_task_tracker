from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str,"%Y-%m-%d")
        return True
    except ValueError:
        return False


#The function will verify the priority the user will input
def get_valid_priority():
    while True:
        p = input("What is the task priority: High/Medium/Low: ").strip().capitalize()

        if p in ["High", "Medium", "Low"]:
            return p

        print("Invalid priority")

#The function will verify the due date the user will input
def get_valid_date(messege):
    while True:
        d_date = input(messege)
        if is_valid_date(d_date):
            return d_date
        print("Invalid date!!, please try again")

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

#The function will verify the category the user will input
def get_valid_category():
    while True:
        p = input("What is the task Category: Study/Work/Personal/Health/Programming").strip().capitalize()

        if p in ["Study","Work","Personal","Health","Programming"]:
            return p

        print("Invalid Category")