# task_manager.py
import os

class TaskManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                tasks = [task.strip() for task in file.readlines()]
                print(f"Nalozil {len(tasks)} opravilo(a) iz {self.file_name}.")
                return tasks
        else:
            return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')
        print(f"Opravila shranjena v {self.file_name}.")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Opravilo '{task}' dodano.")
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("Nic shranjenih opravil.")
        else:
            print("\Trenutna opravila:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def remove_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            removed_task = self.tasks.pop(task_id - 1)
            print(f"Opravilo '{removed_task}' zbrisan.")
            self.save_tasks()
        else:
            print("Neveljavno opravilo.")
