# main.py
from task_manager import TaskManager

def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Dodaj opravilo\n2. Seznam opravil\n3. Brisi opravilo\n4. Izhod")
        choice = input("Vnesite izbiro: ")

        if choice == '1':
            task = input("Vnesite opravilo: ")
            task_manager.add_task(task)     
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_id = int(input("Vnesite stevilo opravila, ki ga hocete zbrisati: "))
            task_manager.remove_task(task_id)
        elif choice == '4':
            print("Izhod...")
            break
        else:
            print("Napacna izbira! Poskusite ponovno.")

if __name__ == "__main__":
    main()