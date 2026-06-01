import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Storage import load_tasks
from Task_C import Task
import Task as T
import Validation as V

#Refreshes all the tasks we have in the listbox
def refresh_listbox():
  task_listbox.delete(0,tk.END)

  for task in tasks:
    task_listbox.insert(tk.END,str(task))
  
#will allow the user to add tasks
def add_task_gui():
   task_name = task_entry.get().strip()
   if not task_name:
    return
   new_task = Task("Checking GUI",False,"Medium","2026-07-31")
   tasks.append(new_task)
   refresh_listbox()
   task_entry.delete(0,tk.END)

#The function will mark tasks as completed
def completed_task_gui():
  selected = task_listbox.curselection()

  if not selected:
    return
  
  index = selected[0]
  tasks[index].completed = True
  T.sort_tasks(tasks)
  refresh_listbox()

#The function will delete selected task
def delete_task_gui():
  selected = task_listbox.curselection()

  if not selected:
    return
  
  index = selected[0]
  tasks.pop(index)
  T.sort_tasks(tasks)
  refresh_listbox()

#The function will open a designated window for the user to edit the task
def open_edit_window_gui():
  #the function will allow us to save the changes
  def save_changes():
    title = title_entry.get().strip()
    priority = priority_comb.get()
    due_date = date_entry.get().strip()

    if not title:
      messagebox.showerror("Error", "Title cannot be empty")
      return
    
    if not V.is_valid_date(due_date):
      messagebox.showerror("Error", "Date must be YYYY-MM-DD")
      return
    
    task.due_date=due_date
    task.title=title
    task.priority = priority

    refresh_listbox()
    edit_window.destroy()

  selected = task_listbox.curselection()

  if not selected:
    return
  
  index = selected[0]
  task=tasks[index]

  edit_window = tk.Toplevel(root)
  edit_window.title("Edit task")
  edit_window.geometry("300x200")

  title_entry = tk.Entry(edit_window)
  date_entry = tk.Entry(edit_window)
  priority_comb = ttk.Combobox(edit_window,values=["High","Medium","Low"], state= "readonly")
  save_button = tk.Button(edit_window,text="Save",command=save_changes)

  tk.Label(edit_window,text="Title:").pack()
  title_entry.pack()

  tk.Label(edit_window,text="Priority:").pack()
  priority_comb.pack()

  tk.Label(edit_window,text="Due date:").pack()
  date_entry.pack()

  save_button.pack(side=tk.LEFT,padx=5,pady=5)

  title_entry.insert(0,task.title)
  priority_comb.set(task.priority)
  date_entry.insert(0,task.due_date)

def open_statistics_window():
  def colse_statistic():
    statistic_window.destroy()
  
  statistic_window = tk.Toplevel(root)
  statistic_window.title("Edit task")
  statistic_window.geometry("800x800")
  title_label = tk.Label(statistic_window,text="Statistics" , font=("Arial",24)) 
  title_label.pack()

  summery_frame =tk.Frame(statistic_window)
  summery_frame.pack(fill=tk.X)
  text_frame = tk.Frame(statistic_window)
  text_frame.pack(fill=tk.BOTH)
  button_frame = tk.Frame(statistic_window)
  button_frame.pack(fill=tk.X, pady=5)

  stat_text = tk.Text(text_frame,font=("Consolas",12),wrap=tk.WORD)
  stat_text.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
  scrollbar = tk.Scrollbar(text_frame)
  scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

  stat_text.config(yscrollcommand=scrollbar.set)
  scrollbar.config(command=stat_text.yview)

  total_tasks = len(tasks)
  completed_total = sum(task.completed for task in tasks)

  tk.Label(summery_frame,text=f'Total tasks: {total_tasks}').pack()
  tk.Label(summery_frame,text=f'Total completed: {completed_total}').pack()
  tk.Label(summery_frame,text=f'Tasks left: {total_tasks-completed_total} tasks').pack()
  tk.Label(summery_frame,text=f'Completiom rate: {T.get_completion_rate(tasks):.1f}%').pack()
  tk.Label(summery_frame,text = f'High priority tasks left: {T.count_priority(tasks,"High")}').pack()
  tk.Label(summery_frame,text = f'Medium priority tasks left: {T.count_priority(tasks,"Medium")}').pack()
  tk.Label(summery_frame,text = f'Low priority tasks left: {T.count_priority(tasks,"Low")}').pack()

  overdue_tasks= T.get_overdue_tasks(tasks)
  due_today= T.get_due_today_tasks(tasks)
  tasks_this_week= T.get_due_this_week_tasks(tasks)
  tk.Label(summery_frame,text = f'Overdue tasks: {len(overdue_tasks)}').pack()
  tk.Label(summery_frame,text = f'Due today: {len(due_today)} tasks').pack()
  tk.Label(summery_frame,text = f'Due this week: {len(tasks_this_week)} tasks').pack()

  stat_text.insert(tk.END,"Overdue Tasks:\n")
  for task in T.get_overdue_tasks(tasks):
    stat_text.insert(tk.END,f'# {task.title}\n')

  stat_text.insert(tk.END,"\n")
  stat_text.insert(tk.END, "Due Today:\n")
  for task in T.get_due_today_tasks(tasks):
    stat_text.insert(tk.END,f'# {task.title}\n')

  stat_text.insert(tk.END,"\n")
  stat_text.insert(tk.END, "Due this WEEK:\n")
  for task in T.get_due_this_week_tasks(tasks):
    stat_text.insert(tk.END,f'# {task.title}\n')
  
  stat_text.insert(tk.END,"\n")
  stat_text.insert(tk.END, "Closest Task:\n")
  stat_text.insert(tk.END,f'# {T.get_closest_task(tasks)[0].title}\n')

  stat_text.config(state="disabled")

  ok_stat_button = tk.Button(button_frame,text="OK",command=colse_statistic)
  ok_stat_button.pack(padx=5,pady=10)




tasks = load_tasks()

root = tk.Tk() #creates the window
root.title("Task Tracker") #sets the title
root.geometry("800x600") #size of the window

title_label = tk.Label(root,text="Task Tracker" , font=("Arial",24)) #creates the label for the window
title_label.pack() #puts the label on the window 

list_frame = tk.Frame(root)
list_frame.pack(fill=tk.BOTH,expand=True)

control_frame = tk.Frame(root)
control_frame.pack(fill=tk.X)

task_listbox = tk.Listbox(list_frame,font=("Consolas",12))
task_listbox.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=5,pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)


task_entry = tk.Entry(control_frame)
task_entry.pack(side=tk.LEFT,padx=5,pady=5)

add_button = tk.Button(control_frame,text="Add task",command= add_task_gui)
add_button.pack(side=tk.LEFT,padx=5,pady=5)

completed_button = tk.Button(control_frame,text="Complete task",command=completed_task_gui)
completed_button.pack(side=tk.LEFT,padx=5,pady=5)

delete_button = tk.Button(control_frame,text="Delete task",command=delete_task_gui)
delete_button.pack(side=tk.LEFT,padx=5,pady=5)

edit_button = tk.Button(control_frame,text="Edit task",command=open_edit_window_gui)
edit_button.pack(side=tk.LEFT,padx=5,pady=5)

statistics_button = tk.Button(control_frame,text="Statistics",command=open_statistics_window)
statistics_button.pack(side=tk.LEFT,padx=5,pady=5)

refresh_listbox()
root.mainloop() #the main loop of the progrem