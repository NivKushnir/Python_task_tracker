import sqlite3
from Task_C import Task

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

#The function will print the tasks in the DB 
def print_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

#The function will laod all the tasks in the DB into a list
def load_tasks_from_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id,title,completed,priority,due_date,category
    FROM tasks
    """)

    rows = cursor.fetchall()

    tasks = []

    # row = (id,title,completed,priority,due_date,category)
    for row in rows:
        task = Task(
            row[1],          # title
            bool(row[2]),    # completed
            row[3],          # priority
            row[4],          # due_date
            row[5],          # category
            row[0]           # id
        )

        tasks.append(task)

    conn.close()

    return tasks

#The function will update a row in the DB
def update_task(task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET title=?,
        completed=?,
        priority=?,
        due_date=?,
        category=?
    WHERE id=?
    """,
    (
        task.title,
        int(task.completed),
        task.priority,
        task.due_date,
        task.category,
        task.id
    ))

    conn.commit()
    conn.close()

#The function will delete a task from DB
def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()

#The function will update the completed value of a task in DB
def mark_completed(completed,task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE tasks 
        SET completed = ? 
        WHERE id=?""",
        (int(completed),task_id))

    conn.commit()
    conn.close()