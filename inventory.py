items = ['pencil','pen','book','glue','sharpener']
stock_counts = [12,0,8,5,3]

inventory = {item: count for item,count in zip(items,stock_counts)}
print("full inventory:",inventory)

in_stock_items = [item for item in items if inventory [item]>0]
print("items in stock:",in_stock_items)

chosen_item = input("what item do you want to buy")

if chosen_item not in inventory or inventory[chosen_item] ==0:
    print(chosen_item,"item is out of stock! stopping checker.")
    exit()

prices = [12,15,4,6,2]
markup = int(input("enter the markup amount to add to every price:"))

marked_up_prices = list(map(lambda p: p + markup , prices))
print("marked up prices",marked_up_prices)

item_index = items.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("price of",chosen_item,"aftermarkup:",chosen_price)

inventory[chosen_price] = inventory[chosen_item] -1
print(chosen_item,"purchased! remaing stock:",inventory[chosen_item])
print("==========SCHOOL ITEM INVENTORY CHECKER===========pen")
