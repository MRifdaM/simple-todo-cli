from task import Task
import textwrap

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        
    def add_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        
    def view_list(self):
        if not self.tasks:
            print("No Task Yet")
            return False
        for task in self.tasks:
            print(task)
            return True
    
    def detail_task(self, task_id):
        detail_task = next((task for task in self.tasks if task.id == task_id), None)
        
        if detail_task:
            status = "Finished" if detail_task.done else "Unfinished"
            print(textwrap.dedent(f"""
            ==== Task Detail ====
            ID      : {detail_task.id}
            Title   : {detail_task.title}
            Desc    : {detail_task.description}
            Status  : {status}
            """))
        else:
            print("Task Not Found")
            
    def remove_task(self, task_id):
        task_id = int(task_id)
        removed_task = next((task for task in self.tasks if task.id == task_id), None)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        
        if removed_task:
            print(f"Task {removed_task.title} has been successfully deleted.")
        else:
            print("Task Not Found")
            
            