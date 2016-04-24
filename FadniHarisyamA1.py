'''
for docstring
'''

print("Items for Hire ")
print("{} items loaded")

menu = ("Menu:\n (L)ist all items\n (H)ire an item\n (R)eturn an item\n (A)dd new item to stock\n (Q)uit")
openItem = open('items.csv', 'r')
readItem = openItem.readlines()
userInput = input(menu).lower()



while True:
    if userInput == "q":
        print ("{} items saved to items.csv")
        break
    elif userInput == "l":
        for words in readItem:
            name, item_desc, cost, status = words.split(",")
        print(readItem)
        userInput = input(menu).lower()












