from toDoList import ToDoList

toDo = ToDoList()

while True:
    print("\n==== To Do List ====")
    print("1.  View All Task")
    print("2.  Add Task")
    print("3.  Remove Task")
    print("4.  Close")
    
    select = input("Select menu : ")
    
    match select:
        case "1":
            exist = toDo.view_list()
            if not exist:
                continue
            
            task_id = input("Enter Task ( x for back): ")
            if task_id.lower() == "x":
                continue
            
            if task_id.isdigit():
                task_id = int(task_id)
                if task_id < 1:
                    continue
                toDo.detail_task(task_id)
                
        case "2":
            title = input("Enter Task Title : ")
            description = input("Enter Description : ")
            toDo.add_task(title, description)
        case "3":
            toDo.view_list()
            task_id = input("Enter Task : ")
            toDo.remove_task(task_id)
        case "4": 
            break
        case _:
            print("Invalid Menu Selection")