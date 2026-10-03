#question number six


def generate_reorder_list(inventory, min_threshold):
    summary = {}
    for item, stock in inventory.items():
        if stock <  min_threshold:
            summary_quantity = 100 - stock
            summary[item]= summary_quantity
    return summary
inventory = {}
num_of_items = int(input("The number of items: "))
for i in range(num_of_items):
    item = input("enter the name of the item: ")
    stock = int(input("enter current stock: "))
    inventory[item] = stock
min_threshold = int(input("enter the minimum stock threshold: "))
result = generate_reorder_list(inventory, min_threshold)
print(result)
       


