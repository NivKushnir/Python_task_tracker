import sqlite3

#Creates a databse for the project
def create_database():
    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,completed INTEGER NOT NULL,priority TEXT NOT NULL,due_date TEXT NOT NULL,category TEXT NOT NULL)""")

    conn.commit()
    conn.close()

#Adds tasks in the DB
def add_task(task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(""" INSERT INTO tasks 
                   (title,completed,priority,due_date,category)
                   VALUES(?,?,?,?,?)""",(task.title,int(task.completed),task.priority,task.due_date,task.category))
    
    conn.commit()
    conn.close()

def print_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()