tasks = []


def main():
    print("\t YOUR TO DO LIST")
    menu()


def option_1():
    # Add new tasks
    print("\t ADD TASK")
    print("\t----------")
    new_task = input("New task: ")
    tasks.append(new_task + "\n")
    add_to_file()
    menu()


def add_to_file():
    # adding the user's task to a file
    f = open("current_tasks.txt", "w+")
    f.writelines(tasks)


def option_2():
    # Mark task as complete
    f = open("current_tasks.txt", "r")
    print(f.read())

    user = input("What have you completed: ")

    with open("current_tasks.txt", 'r') as firstfile, open("completed_tasks.txt", 'a') as secondfile:
        for _ in firstfile:
            secondfile.write(user)

    menu()


def option_3():
    # Delete task

    print()


def option_4():
    # View tasks
    for i in tasks:
        print(i)
    print()


def option_5():
    # view completed tasks
    print()


def option_6():
    # exit
    print()


def menu():
    print("""
        1. Add tasks
        2. Mark tasks as complete
        3. Delete tasks
        4. View tasks
        5. View completed task
        6. Exit
    """)
    option = int(input("What would you like to do?: "))
    print()

    if option == 1:
        option_1()
    elif option == 2:
        option_2()


main()
