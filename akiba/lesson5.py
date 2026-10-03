customer_name = input("The name of the customer? ")
product_name = input("The name of the product? ")
price = float(input("The price of the product: "))
quantity = int(input("How many products: "))
total_price = price * quantity;
print(f'''=======================================
          RECEIPT
=======================================
Customer: {customer_name}
Product \t Price \t Qty
---------------------------------------
{product_name}\t{price}ETB\t{quantity}
Total: {total_price}ETB

Thank you for shopping!
=======================================''')
