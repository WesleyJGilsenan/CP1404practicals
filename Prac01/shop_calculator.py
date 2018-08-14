total = 0
itemnum = int(input("How many items do you have? "))

while itemnum < 0:
    print("Invalid number of items!")
    itemnum = int(input("How many items do you have? "))

for i in range(itemnum):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total = total * 0.9

print("Total price for ", itemnum, " items is $", total)