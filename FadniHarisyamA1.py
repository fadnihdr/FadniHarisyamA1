'''
for docstring
'''

openItem = open('items.csv', 'r')
readItem = openItem.readlines()

for i in readItem:
    name, item_desc, cost, status = i.split(",")
    print(name, item_desc, cost, status)


