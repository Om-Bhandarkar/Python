
num_items = int(input("How many items do you want to list? "))
items = []
for i in range(num_items):
    item = input(f"Enter item {i + 1}: ")
    items.append(item)


print("List of items: {} ".format(items))
# print(f"List of items: {items} ")


