n = int(input())
maxCost = 0
maxCostItem = ""
avg = 0
totalCost = 0
for i in range(n):
    item = input()
    quantity = int(input())
    price = int(input())
    totalCost = totalCost + (price * quantity)

    if totalCost > maxCost:
        maxCostItem = item
    avg = totalCost / (i+1)

print("Item: {} \nTotal price: {:.2f}\n Average Price: {:.2f}".format(maxCostItem, totalCost, avg))
