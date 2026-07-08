class to_do_list:
    def __init__(self):
        self.tasks = [] 

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Added task: "{task}".end=')
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        print("--- To-Do List ---")
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f'{i}. {task["task"]} — {status}')
            print("keep on going")
    def delete_tasks(self):
        
