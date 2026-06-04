import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Storage import load_tasks,save_tasks
from Task_C import Task
import Task as T
import Validation as V
from datetime import  datetime

def on_closing():
  save_tasks(tasks)
  root.destroy()

#The function will show Error msg
def show_error(msg):
  messagebox.showerror("Error", msg)

#Refreshes all the tasks we have in the listbox
def refresh_listbox():
  task_listbox.delete(0,tk.END)

  for task in tasks:
    task_listbox.insert(tk.END,str(task))

def open_add_window(): 
  #the function will allow us to save the changes
  def save_changes():
    title = title_entry.get().strip()
    priority = priority_comb.get()
    due_date = date_entry.get().strip()

    if not title:
      show_error("Title cannot be empty")
      return
    
    if not V.is_valid_date(due_date):
      show_error("Date must be YYYY-MM-DD")
      return
    
    tasks.append(Task(title,False,priority,due_date))
    T.sort_tasks(tasks)

    refresh_listbox()
    add_window.destroy()


  add_window = tk.Toplevel(root)
  add_window.title("Add Task")
  add_window.geometry("300x200")

  title_entry = tk.Entry(add_window)
  date_entry = tk.Entry(add_window)
  priority_comb = ttk.Combobox(add_window,values=["High","Medium","Low"], state= "readonly")
  priority_comb.current(1)
  save_button = tk.Button(add_window,text="Save",command=save_changes)

  tk.Label(add_window,text="Title:").pack()
  title_entry.pack()

  tk.Label(add_window,text="Priority:").pack()
  priority_comb.pack()

  tk.Label(add_window,text="Due date:").pack()
  date_entry.pack()

  save_button.pack(pady=10)

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
  d_task=tasks[index]
  if messagebox.askyesno("Delete Task",f"Delete '{d_task.title}'?"):
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
      show_error("Title cannot be empty")
      return
    
    if not V.is_valid_date(due_date):
      show_error("Date must be YYYY-MM-DD")
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

#The function will open awindow with all the user statistics
def open_statistics_window():
  def colse_statistic():
    statistic_window.destroy()

  def add_tasks(text_widget,title,tasks):
    text_widget.insert(tk.END,f'========== {title} ==========\n')
    if not tasks:
      text_widget.insert(tk.END,"!!!NONE!!!\n")
    for task in tasks:
      text_widget.insert(tk.END,f'{task.title}\n')
  
  statistic_window = tk.Toplevel(root)
  statistic_window.title("Statistics")
  statistic_window.geometry("800x800")
  title_label = tk.Label(statistic_window,text="Statistics" , font=("Arial",24)) 
  title_label.pack()

  summery_frame =tk.Frame(statistic_window)
  summery_frame.pack(fill=tk.X)
  text_frame = tk.Frame(statistic_window)
  text_frame.pack(fill=tk.BOTH,expand=True)
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

  add_tasks(stat_text,"Overdue Tasks",T.get_overdue_tasks(tasks))
  stat_text.insert(tk.END,"\n")

  add_tasks(stat_text,"Due Today",T.get_due_today_tasks(tasks))
  stat_text.insert(tk.END,"\n")

  add_tasks(stat_text,"Due this week",T.get_due_this_week_tasks(tasks))
  stat_text.insert(tk.END,"\n")

  stat_text.insert(tk.END, "========== Closest Task ==========\n")
  stat_text.insert(tk.END,f'# {T.get_closest_task(tasks)[0].title}\n')

  stat_text.config(state="disabled")

  ok_stat_button = tk.Button(button_frame,text="OK",command=colse_statistic)
  ok_stat_button.pack(pady=10)


def open_search_window():
  #The function will update the input for each category
  def update_search_input(event=None):
    search_entry.pack_forget()
    p_comb.pack_forget()
    start_date_entry.pack_forget()
    end_date_entry.pack_forget()
    input_label.pack_forget()
    end_date_title.pack_forget()

    choice = search_comb.get()

    if choice == "Title":
      input_label.config(text="Tittle:")
      input_label.pack()
      search_entry.pack()

    elif choice == "Priority":
      input_label.config(text="Priority:")
      input_label.pack()
      p_comb.pack()
    
    elif choice == "Date":
      input_label.config(text="Start date:")
      input_label.pack()
      start_date_entry.pack()
      end_date_title.config(text="End date")
      end_date_title.pack()
      end_date_entry.pack()
  
  #The function will perform our search
  def perform_search():
    res_listbox.delete(0,tk.END)
    choice = search_comb.get()

    if choice == "Title":
      keyword = search_entry.get().strip()
      if not keyword:
        show_error("Search text cannot br empty!")
        return
      
      res = T.search_by_title(tasks,keyword)

    elif choice == "Priority":
      p = p_comb.get()
      if not p:
        show_error("Please select a priority!")
        return
      
      res = T.search_by_priority(tasks,p)

    elif choice == "Date":
      start_date = start_date_entry.get().strip()
      end_date = end_date_entry.get().strip()
      
      if not V.is_valid_date(start_date):
        show_error("Start date must be YYYY-MM-DD!")
        return
      
      if not V.is_valid_date(end_date):
        show_error("End date must be YYYY-MM-DD")
        return
      
      start_date = datetime.strptime(start_date,"%Y-%m-%d").date()
      end_date = datetime.strptime(end_date,"%Y-%m-%d").date()

      if end_date<start_date:
        show_error("End date must be after start date")
        return
      
      res = T.search_by_date_range(tasks,start_date,end_date)
    
    if not res:
      messagebox.showinfo("Search","No matching tasks found")
      return
    
    for task in res:
      res_listbox.insert(tk.END,str(task))




  search_window = tk.Toplevel(root)
  search_window.title("Search Tasks")
  search_window.geometry("500x250")
  title_label = tk.Label(search_window,text="Search" , font=("Arial",24)) 
  title_label.pack()


  search_comb = ttk.Combobox(search_window,values=["Title","Priority","Date"], state= "readonly")
  tk.Label(search_window,text="Search by: ").pack()
  search_comb.pack()

  input_frame = tk.Frame(search_window)
  input_frame.pack()

  input_label = tk.Label(input_frame,text="")
  end_date_title = tk.Label(input_frame,text="")
  search_entry = tk.Entry(input_frame)
  p_comb = ttk.Combobox(input_frame,values=["High","Medium","Low"], state= "readonly")
  start_date_entry = tk.Entry(input_frame)
  end_date_entry = tk.Entry(input_frame)
  search_comb.bind("<<ComboboxSelected>>",update_search_input)
  search_comb.current(0)
  update_search_input() 

  res_search_button =tk.Button(search_window,text="Search",command = perform_search)
  res_search_button.pack(pady=5)

  res_frame = tk.Frame(search_window)
  res_frame.pack(fill=tk.BOTH,expand=True,padx=5,pady=5)

  res_listbox=tk.Listbox(res_frame,font=("Consolas",12))
  res_listbox.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

  res_scrollbar = tk.Scrollbar(res_frame)
  res_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

  res_listbox.config(yscrollcommand=res_scrollbar.set)

  res_scrollbar.config(command=res_listbox.yview)

  
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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

add_button = tk.Button(control_frame,text="Add task",command= open_add_window)
add_button.pack(side=tk.LEFT,padx=5,pady=5)

completed_button = tk.Button(control_frame,text="Complete task",command=completed_task_gui)
completed_button.pack(side=tk.LEFT,padx=5,pady=5)

delete_button = tk.Button(control_frame,text="Delete task",command=delete_task_gui)
delete_button.pack(side=tk.LEFT,padx=5,pady=5)

edit_button = tk.Button(control_frame,text="Edit task",command=open_edit_window_gui)
edit_button.pack(side=tk.LEFT,padx=5,pady=5)

statistics_button = tk.Button(control_frame,text="Statistics",command=open_statistics_window)
statistics_button.pack(side=tk.LEFT,padx=5,pady=5)

search_button = tk.Button(control_frame,text="Search",command=open_search_window)
search_button.pack(side=tk.LEFT,padx=5,pady=5)

refresh_listbox()

root.protocol("WM_DELETE_WINDOW",on_closing)

root.mainloop() #the main loop of the progrem