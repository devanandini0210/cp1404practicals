number_of_items = int(input("Number of items: "))
total = 0

for i in range(0,number_of_items,1):
    price_of_item = float(input("Price of item :"))
    total = total+price_of_item

if total>100:
    total = total - (0.1*total)
print("Total price for "+str(number_of_items)+" is "+str("%.2f" % total))

