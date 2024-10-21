# task_manager.py
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nCurrent tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def remove_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            removed_task = self.tasks.pop(task_id - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
