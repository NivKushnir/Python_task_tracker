class Task:
    def __init__(self,title,completed,priority,due_date):
        self.title = title
        self.completed = completed
        self.priority = priority
        self.due_date = due_date
    
    def to_dict(self):
        return {"title": self.title, "completed": self.completed,"priority": self.priority,"due_date": self.due_date}
    
    @classmethod
    def from_dict(cls,data):
        return cls(data["title"],data["completed"],data["priority"],data["due_date"])