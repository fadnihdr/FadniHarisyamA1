'''
Name: Fadni Harisyam
ID: 13269323
Date:23/04/2016
Program Detail: This program will be used for hiring items, adding them and should be able to modify its status.
'''

num_lines = sum(1 for line in open('items.csv'))
"""count the lines in a file"""
print("Items for Hire - by Fadni Harisyam\n{} items loaded".format(num_lines))


menu = ("Menu:\n (L)ist all items\n (H)ire an item\n (R)eturn an item\n (A)dd new item to stock\n (Q)uit")
"""this will be my main menu"""
openItem = open('items.csv', 'r')
userInput = input(menu).lower() #all inputs will be treated as lowercase


def item_list():
    item_num = 0
    with open('items.csv') as items:
        for words in items:
            name,item_desc,cost,status = words.split(',')
            if "in" in status:
                print("{:} - {:<40s} = ${:>7,.2f}".format(item_num, name + "(" + item_desc + ")", float(cost)))
            elif 'out' in status:
                print("{:} - {:<40s} = ${:>7,.2f} *".format(item_num, name + "(" + item_desc + ")", float(cost)))
            item_num += 1
    items.close()
    """
    A function to load and show items from the csv file

    and will remove the commas, removing 'in' and replacing 'out' with an asterisk '*'

    the values for each line are name,item_desc,cost,status
    """


def item_hire():
    item_count = 0
    list_num = []
    line_list = list()
    with open('items.csv') as file:
        item_lines_list = file.readlines()
    for index, line in enumerate(item_lines_list):
        line_list.append(line)
        name, item_desc, price, hire = line_list[index].split(',')
        if 'in' in hire:
            print("{:} - {:<40s} = ${:>7,.2f}".format(item_count, name + " (" + item_desc + ") ", float(price)))
            list_num.append(item_count)
        item_count += 1

    if len(list_num) == 0:
        print("Currently no item is available to hire")
    else:
        try:

            replace = int(input("Enter the number of an item to hire:\n"))
            if replace in list_num:
                item_lines_list[replace] = item_lines_list[replace].replace('in', 'out')
                with open('items.csv', 'w') as file:
                    file.writelines(item_lines_list)
                    name, desc, price, hire = line_list[replace].split(',')
                    print("{} is hired for ${:.2f}".format(name, float(price)))
            else:
                print("That item is not available for hire\n")
        except:
            print("Invalid input")

def item_return():
    item_count = 0
    list_num = []
    line_list = list()
    with open('items.csv') as file:
        item_lines_list = file.readlines()
    for index, line in enumerate(item_lines_list):
        line_list.append(line)
        name, desc, price, hire = line_list[index].split(',')
        if 'out' in hire:
            print("{:<3d} - {:<40s} = ${:>7,.2f} *".format(item_count, name + " (" + desc + ") ", float(price)))
            list_num.append(item_count)
        item_count += 1

    else:
        try:

            replace = int(input("Enter the number of an item to return:\n"))
            if replace in list_num:
                item_lines_list[replace] = item_lines_list[replace].replace('out', 'in')
                with open('items.csv', 'w') as file:
                    file.writelines(item_lines_list)
                    name, desc, price, hire = line_list[replace].split(',')
                    print(name, "returned.")
            else:
                print("Item is not available.\n")
        except:
            print("Invalid input")

    file.close()  # every file needs to be closed after their job is done


while True: #when the user enters "q" it will end the program
    if userInput == "q":
        print ("{} items saved to items.csv".format(num_lines))
        break


    elif userInput == "l": #when the user enters "l" it will call the item_list() function
        item_list()
        userInput = input(menu).lower()


    elif userInput == "h": #when the user enters "h" it will call the item_hire() function
        item_hire()
        userInput = input(menu).lower()


    elif userInput == "a":
        """when the user enters "a" it will ask the user's item name,
                    description, and cost, and add them to the csv file"""
        name = (input("Name:"))
        while len(name)<=0:
            print("Please input a valid name")
            name = (input("Name:"))
        item_desc = (input("Description:"))
        while len(item_desc)<=0:
            print("Please input a valid description")
            item_desc = (input("Description:"))
        try: #to error check the cost by putting a ValueError exception
            cost = int(input("Cost:"))
        except ValueError:
            print("Please enter a valid integer")
            cost = int(input("Cost:"))
        items_write = open('items.csv', 'a')
        print((name + "," + item_desc + "," + str(cost) + "," + "in"), file=items_write)
        items_write.close()
        print(name, item_desc, cost)
        print("\n{} ({}), ${:.2f} now available for hire.".format(name, item_desc, cost))
        userInput = input(menu).lower()
        num_lines += 1


    else:
        item_return()
        userInput = input(menu)













