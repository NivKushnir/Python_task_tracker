import sqlite3

def create_database():
    conn = sqlite3.connect("tasks.db")

    crusor = conn.cursor()

    crusor.execute(""" CREATE TASBLE IF NOT EXIST tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,completed INTEGER NOT NULL,priority TEXT NOT NULL,due_date TEXT NOT NULL,category TEXT NOT NULL)""")

    conn.commit()
    conn.close()