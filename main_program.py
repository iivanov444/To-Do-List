import random

def main():

    def add_new_task():    
        while True:
            print("To exit, use 'exit'")
            print("To enter task editing, use command 'add'")
            task = input()
            if task != "add" and task != "exit":
                print("Invalid input. Allowed: 'add' and 'done'.")
            elif task == "exit":
                break
            else:
                print("Use 'done' when you finish adding tasks.")
                while True:
                    task = input("Enter a task: ")
                    if task == "done":
                        break
        
                    task_list.append({'task': task, 'completed': False})
                    print(f'Task "{task}" added successfully!')
        return to_do_menu()
 
 
    def mark_task_completed():
        index = int(input("Enter the index of the task to mark as completed: "))
    
        if 1 <= index <= len(task_list):
            task_list[index - 1]['completed'] = True
        else:
            print("Task not in range")
        return to_do_menu()


    def view_tasks():
        print("##### Tasks #####")
        for i, task in enumerate(task_list):
            i += 1
            status = '[X]' if task['completed'] else '[ ]'
            print(f"Index {i}. {status} {task['task']}")
        return to_do_menu()    


    def clean():
        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \
        \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
        return to_do_menu()


    def to_do_menu():
        print("##### To-Do List Menu #####\
        \n 1. Add a new task\
        \n 2. Mark a task as completed\
        \n 3. View all tasks\
        \n 4. Clean\
        \n 5. Quit")
        user_choice = int(input("Enter your choice (1-5): "))
        while True:
            if user_choice not in range(1,6):
                print("Invalid input. Choose from (1-5)")
            elif user_choice == 1:
                add_new_task()
            elif user_choice == 2:
                mark_task_completed()
            elif user_choice == 3:
                view_tasks()
            elif user_choice == 4:
                clean()
            elif user_choice == 5:
                exit_msgs = ["See you soon!", "Bye bye!", "Have a pleasant day!", "Have a successful day!"]
                random_exit_msg = random.choice(exit_msgs)
                raise SystemExit(random_exit_msg)
            user_choice = int(input("Enter your choice (1-4): "))

            
    task_list = []
    to_do_menu()
    
if __name__ == '__main__':
    main()