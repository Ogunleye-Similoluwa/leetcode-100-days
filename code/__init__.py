import time, os

general_list =[]

f = open("calender.txt", "r")
general_list = eval(f.read())
f.close()


def menu():
    active = True
    while active:
        menu = int(input("""
    Press 1 -> Add
    Press 2 -> View
    Press 3 -> Remove
    Press 4 -> Edit
    Press 5 -> Exit
    """))
        if menu == 1:
            add()
        elif menu == 2:
            view()
        elif menu == 3:
            remove()
        elif menu == 4:
            edit()
        elif menu == 5:
                break
    time.sleep(1)
    os.system("clear")


def add():
    time.sleep(1)
    os.system("clear")
    name = input("Name > ")
    date = input("Due Date > ")
    priority = input("Priority > ").capitalize()
    my_list = [name, date, priority]
    general_list.append(my_list)
    print("Added")


def view():
    time.sleep(1)
    os.system("clear")
    count = 1
    my_menu = int(input("""
    Press 1 -> View all
    Press 2 -> View priority
  """))
    if my_menu == 1:
        for item in general_list:
            for ids in item:
                print(ids + " | ", end="")
                if count == 3:
                    print()
                count += 1
    elif my_menu == 2:
        menu_2 = int(input("""
    Press 1 -> View High
    Press 2 -> View Medium
    Press 3 -> View Low
  """))
        if menu_2 == 1:
            for item in general_list:
                for ids in item:
                    if "High" in item:
                        print(ids + " | ", end="")
                    else:
                        print("Item not in list")
                        menu()


        elif menu_2 == 2:
            for item in general_list:
                for ids in item:
                    if "Medium" in item:
                        print(ids + " | ", end="")
                    else:
                        print("Item not in list")
                        menu()


        elif menu_2 == 3:
            for item in general_list:
                if "Low" in item:
                    print(item + " | ", end="")
                else:
                    print("Item not in list")
                    menu()

        elif general_list is None:
            print("No item in list")
            menu()


def edit():
    time.sleep(1)
    os.system("clear")
    find = input("Name of todo to edit > ")
    found = False
    for row in general_list:
        if find in row:
            found = True
    if not found:
        print("Couldn't find that")
        return
    for row in general_list:
        if find in row:
            general_list.remove(row)
    name = input("Name > ")
    date = input("Due Date > ")
    priority = input("Priority > ").capitalize()
    row = [name, date, priority]
    general_list.append(row)
    print("Added")


def remove():
    time.sleep(1)
    os.system("clear")
    find = input("Name of todo to remove > ")
    for row in general_list:
        if find in row:
            general_list.remove(row)


menu()
p = open("calender.txt", "w")
p.write(str(general_list))
p.close()
