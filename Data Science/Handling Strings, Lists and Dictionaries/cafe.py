"""Program to calculate cafe stock, price and calculate the total stock"""

# 1. create a list with 4-6 items called menu
# 2. create a dictionary called stock, with value of above items
# 3. create another dictionary named price, with prices for each item
# 4. calculate item value for 5 item, use forumula for item_value = (stock[items] * price[items])
# 5. calculate the total_stock worth in the café (cost of each item and add them all)
# 6. print results of calculation

# 1. menu list containing 5 items
menu = ['Soup', 'Scone', 'Cake', 'Brownie', 'Cheese Sandwich']


# 2. dictionary called stock for 5 menu items
stock = {
    'Soup': 14,
    'Scone': 10,
    'Cake': 17,
    'Brownie': 16,
    'Cheese Sandwich': 18
    }


# 3. another dictionary called price for prices of 5 menu items
price = {
    'Soup': 5,
    'Scone': 3,
    'Cake': 4,
    'Brownie': 4,
    'Cheese Sandwich': 6 
}
print(f'Price of each item: {price}\n')

# 4. calculate total item value of each of 5 items and assing/print it in new dictionary
item_value = {}
for key in stock:
    item_value[key] = stock[key] * price[key]
print(f'Total value of 5 items: {item_value}')


#5. calculate the total_stock worth in the café, by suming all value in item_value dictionary
total_stock = sum(item_value.values())


#6. print result of total_stock for all 5 items
print(
    f"""\n==================================================
    
    Cafe's total stock value is : {total_stock}
    \n===================================================""")
