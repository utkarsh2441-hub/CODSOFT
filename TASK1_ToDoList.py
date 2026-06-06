task = []
while True:
    print("\n--To Do List--")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Complete Tasks")
    print("4. Exit")

    choice=input("Enter choice: ")
    if choice == "1":
        task_input=input("Enter Task: ")
        task.append(task_input)
        print("Task Added")
    elif choice=="2":
        if len(task)==0:
            print("No task available")
        else:
            print("\nYour tasks: ")
            for i in range(len(task)):
                print(i+1,".",task[i])
    elif choice == "3":
        if len(task)==0:
            print("No tasks available")
        else:
            for i in range(len(task)):
                print(i+1,".",task[i])

            num=int(input("Enter task number Completed: "))

            if 1<= num <= len(task):
                completed=task.pop(num-1)
                print(completed,"Completed")
            else:
                print("Invalid Number")

    elif choice=="4":
        print("Program Closed")
        break
    else:
        print("Invalid Choice")

    from datetime import datetime

    task_input=input("Enter task: ")
    time=datetime.now().strftime("%d-%m-%y %H:%M")
    task.append(task_input+" Added: "+ time)







