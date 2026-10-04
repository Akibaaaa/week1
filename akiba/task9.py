amount_in_USD = float(input("Enter amount in USD: "))
exchange_rate = 150
amount_in_ETB = amount_in_USD * exchange_rate
print("=================================================")
print("          CURRENCY EXCHANGE                      ")
print("=================================================")
print(f'''USD Amount: {amount_in_USD}
Exchange Rate: 1 USD = {exchange_rate} ETB
ETB Amount: {amount_in_ETB} ETB
=================================================''')

# Allowing the user to input the exchange rate 
#exchange_rate= float(input("Enter exchange rate: "))
#amount_in_ETB = amount _in_USD * exchange_rate