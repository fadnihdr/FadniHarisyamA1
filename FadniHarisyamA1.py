'''
for docstring
'''

print("Items for Hire ")
print("{} items loaded")

menu = ("Menu:\n (L)ist all items\n (H)ire an item\n (R)eturn an item\n (A)dd new item to stock\n (Q)uit")
openItem = open('items.csv', 'r')
readItem = openItem.readlines()
userInput = input(menu).lower()

def item_list():
    item_count = 0
    with open('items.csv') as items:
        for words in readItem:
            name,item_desc,cost,status = words.split(',')
            if "in" in status:
                print("{:<3d} - {:<40s} = ${:>7,.2f} ".format(item_count, name + item_desc + ")", float(cost)))
            elif 'out' in status:
                print("{:}   - {:} = ${:>7,.2f} *".format(item_count, name + item_desc + ")", float(cost)))
            item_count += 1
    items.close()





while True:
    if userInput == "q":
        print ("{} items saved to items.csv")
        break
    elif userInput == "l":
        item_list()
        userInput = input(menu).lower()












