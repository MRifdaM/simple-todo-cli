class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.done = False
    
    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.id}. {self.title}"
    
    def mark_as_done(self):
        self.done = True