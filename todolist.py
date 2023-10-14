from tkinter import *
from colorama import Fore, Style

tasks = []

# background = "#ADD8E6" # light blue
# framebg = "#EDEDED"
# framefg = "#06283D"
#
# root = Tk()
# root.title("Note Pad")
# root.geometry("400x500+210+100")
# root.config(bg=background)
#
#
# # top frame
# top_frame = Label(root, text="YOUR TO-DO LIST",
#                   width=10, height=3,
#                   bg="red", anchor="center",
#                   font=("Poppins", 15))
# top_frame.pack(fill=X)







# root.mainloop()









def main():
    print("\t YOUR TO DO LIST")
    menu()


def option_1():
    # Add new tasks
    print("\t ADD TASKS")
    print("\t----------")
    new_task = input("New task: ")
    if new_task == "":
        print(Fore.RED + "field empty \n")
        print(Style.RESET_ALL)
        option_1()
    else:
        tasks.append(new_task + "\n")
        add_to_file()
        menu()


def add_to_file():
    # adding the user's task to a file

    # reads file and stroes it in fileread
    f = open("current_tasks.txt", "r")
    fileread = f.read()

    # If file is not empty
    if len(fileread) > 0:
        f = open("current_tasks.txt", "a")
        # adding the last text entered not the whole array
        task = tasks[(len(tasks) - 1)]
        f.write(task)

    else:
        f = open("current_tasks.txt", "w")
        f.writelines(tasks)


def read_current_file():
    count = 0
    f = open("current_tasks.txt", "r")
    lines = f.readlines()

    for line in lines:
        count += 1
        print("{}. {}".format(count, line.strip("\n")))


def read_completed_file():
    count = 0
    f = open("completed_tasks.txt", "r")
    lines = f.readlines()

    for line in lines:
        count += 1
        print("{}. {}".format(count, line.strip("\n")))


def option_2():
    # initialize count
    count = 0

    # read file and store in lines
    f = open("current_tasks.txt", "r")
    lines = f.readlines()

    if len(lines) == 0:
        print("No Tasks To Complete")

    else:

        for line in lines:
            # count every line starting from 1
            count += 1

            # The format (e.g. 1. cook)
            print("{}. {}".format(count, line.strip("\n")))

        user = int(input("What have you completed:"))

        # to get the current index
        useno = user - 1

        # getting the value with its index
        valiwant = lines[useno]

        # remove value I want from lines in current_task
        lines.remove(valiwant)

        # clear and rewrite everything in lines array except from valiwant
        f = open("current_tasks.txt", "w")
        f.writelines(lines)
        f.close()

        print(valiwant.strip("\n") + " completed 🌈🌈")

        # push to completed task (appends)
        f = open("completed_tasks.txt", "a")
        f.write(valiwant)
        f.close()

    menu()


def option_3():
    count = 0

    # Delete task

    with open("current_tasks.txt", "r") as fp:
        lines = fp.readlines()

    for rline in lines:
        # count every line starting from 1
        count += 1

        # The format (e.g. 1. cook)
        print("{}. {}".format(count, rline.strip("\n")))

    delete = int(input("Which task would you like to delete: "))



    menu()


def option_4():
    # View tasks
    print("\t TO-DO LIST")
    read_current_file()
    menu()


def option_5():
    # view completed tasks
    print("\t COMPLETED TASKS")
    read_completed_file()
    menu()


def option_6():
    # exit
    print("Goodbye")
    exit()


def menu():
    print("""
            MENU
        ------------
        1. Add tasks
        2. Mark tasks as complete
        3. Delete tasks
        4. View tasks
        5. View completed task
        6. Exit
    """)

    option = int(input("What would you like to do?: "))
    print(f"Option {option}: ")
    print()

    try:
        fun = globals()["option_" + str(option)]
        fun()
    except KeyError:
        print(f"There is no option_{option}")
        menu()


    def options():
        if option == 1:
            option_1()
        elif option == 2:
            option_2()
        elif option == 3:
            option_3()
        elif option == 4:
            option_4()
        elif option == 5:
            option_5()
        elif option == 6:
            option_6()
        else:
            print("option not available")
            menu()

main()
read_current_file()
read_completed_file()
