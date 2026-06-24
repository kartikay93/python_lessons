print("Welcome! to your aaplication")

tasks = []

while True:
    enter = input(print("Choose the option among these:" \
    "\n1. Add new task \n2. Show tasks \n3. Completed Tasks \n4. Remove tasks \n5. Clear all tasks \n6. Exit"))


    if enter == "1" or enter.lower() == "add new task":
        while True:
            new_task = input("Enter the new task(or type 'exit' to return): ")
            if new_task.lower() in ["exit", "save", "", " "]:
               break
            else:
                tasks.append(new_task)
                print(f"New task added: {new_task}")
            
    elif enter == "2" or enter.lower() == "show tasks":
        if not tasks:
            print("Your task list is empty!")
        else:
            print("\nTasks are: ")

            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    #print(f"Tasks are: {tasks}")
        comp = input("Do you want to mark a task as completed: yes/no: ").lower().strip()
        if comp == "yes":
            try:
                num = int(input("Which task you want to mark as completed (Enter the serial no.):"))
                num = num-1
                if 0 <= num < len(tasks):
                    if " <-- completed" not in tasks[num]:
                        tasks[num] = tasks[num] + " <-- completed"
                        print("Task marked as completed!")
                    else:
                        print("This task is already completed.")
                else:
                    print("Invalid Serial number.")
            except ValueError:
                print("Please enter a valid number.")
        #while True:
        #    if num in tasks.index():
        #        tasks[num] = tasks[num]+ " <--    completed"
        #        
        #    else:
        #        print("Enter valid task no.")
        #        num = int(input("Enter task no. again: "))


    elif enter == "3" or enter.lower() == "completed tasks":
        completed = [t for t in tasks if "completed" in t]
        if completed:
            print("\nCompleted tasks:")
            for t in completed:
               print(t)
        else:
            print("No complted task found.")


    elif enter == "4" or enter.lower() == "remove tasks":
        if not tasks:
            print("No tasks to remove..")
        else:
            print("Current task list: ")
            for i, task in enumerate(tasks,1):
                print(f"{i}. {task}")
            try:
                sr_no = int(input("Enter the serial no. of the task to remove: ")) - 1
                if 0 <= sr_no < len(tasks):
                    removed = tasks.pop(sr_no)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid serial number.")
            except ValueError:
                print("Please enter a valid number.")
            #tasks.remove(sr_no)
            #print(f"New task list: {tasks}")
    elif enter == "5" or enter.lower() == "clear all tasks":
        while True :
            word = input("Are you confirm to clear all tasks: yes/no").lower().strip()
            if word == "yes":
                tasks.clear()
                print("Task List is cleared")
                break
            elif word == "no":
                print(" Action Cancelled ")
                break
            else:
                print("Invalid! Please, Enter only yes or no: ")
    
    elif enter == "6" or enter.lower() == "exit":
        print("Goodbye!")
        break
    
    else:
        print("Please choose a valid number among the options.")