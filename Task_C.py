class Task:
    def __init__(self,title,completed,priority):
        self.title = title
        self.completed = completed
        self.priority = priority
    
    def to_dict(self):
        return {"title": self.title, "completed": self.completed,"priority": self.priority}
    
    @classmethod
    def from_dict(cls,data):
        return cls(data["title"],data["completed"],data["priority"])