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
        for words in readItem:
            name,item_desc,cost,status = words.split(',')
            if "in" in status:
                print("{:} - {:<40s} = ${:>7,.2f}".format(item_num, name + "(" + item_desc + ")", float(cost)))
            elif 'out' in status:
                print("{:} - {:<40s} = ${:>7,.2f} *".format(item_num, name + "(" + item_desc + ")", float(cost)))
            item_num += 1
    items.close()



def item_hire():
    item_count = 0
    with open('items.csv') as items:
        items_line = items.readlines()
        user_hire = input("Enter the number of item to hire")



while True:
    if userInput == "q":
        print ("{} items saved to items.csv")
        break
    elif userInput == "l":
        item_list()
        userInput = input(menu).lower()
    elif userInput == "h":
        hireInput = str(input('\n'))
        item_hire(hireInput)
        item_list()
        userInput = input(menu).lower()














