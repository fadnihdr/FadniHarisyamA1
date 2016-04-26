'''
for docstring
'''

num_lines = sum(1 for line in open('items.csv'))  #count the lines in a file(src = http://prntscr.com/awh2eh)
print("Items for Hire - by Fadni Harisyam\n{} items loaded".format(num_lines)) #shows the amount of lines in a file

menu = ("Menu:\n (L)ist all items\n (H)ire an item\n (R)eturn an item\n (A)dd new item to stock\n (Q)uit")
openItem = open('items.csv', 'r')
readItem = openItem.readlines()
userInput = input(menu).lower()


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


def item_hire():
    item_count = 0
    list_num = []
    line_list = list()
    with open('items.csv') as file:
        item_lines_list = file.readlines()
    for index, line in enumerate(item_lines_list):
        line_list.append(line)
        name, desc, price, hire = line_list[index].split(',')
        if 'in' in hire:
            print("{:<3d} - {:<40s} = ${:>7,.2f}".format(item_count, name + " (" + item_desc + ") ", float(cost)))
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
                    name, item_desc, cost, status = line_list[replace].split(',')
                    print("{} is hired for ${:.2f}".format(name, float(status)))
            else:
                print("That item is not available for hire\n")
        except:
            print("Invalid input")


def item_rent():
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


while True:
    if userInput == "q":
        print ("{} items saved to items.csv".format(num_lines))
        break


    elif userInput == "l":
        item_list()
        userInput = input(menu).lower()


    elif userInput == "h":
        item_list()
        item_hire()
        userInput = input(menu).lower()


    elif userInput == "a":
        name = (input("Name:"))
        while len(name)<=0:
            print("Please input a valid name")
            name = (input("Name:"))
        item_desc = (input("Description:"))
        while len(item_desc)<=0:
            print("Please input a valid description")
            item_desc = (input("Description:"))
        try:
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
        item_list()
        item_rent()
        userInput = input(menu)













