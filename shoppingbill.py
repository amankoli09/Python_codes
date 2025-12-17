# taking inputs
product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
member = int(input("Are you a member? (1 for Yes, 0 for No): "))

# calculations
total_cost = price * quantity

if member == 1:
    discount = total_cost * 0.10   # 10% discount
else:
    discount = 0

final_amount = total_cost - discount

# printing bill
print("\n----- Shopping Bill -----")
print("Product name   :", product_name)
print("Price          :", price)
print("Quantity       :", quantity)
print("Total Cost     :", total_cost)
print("Final Amount   :", final_amount)

# printing data types
print("\n----- Data Types -----")
print("Type of product_name =", type(product_name))
print("Type of price         =", type(price))
print("Type of quantity      =", type(quantity))
print("Type of member        =", type(member))
print("Type of total_cost    =", type(total_cost))
print("Type of final_amount  =", type(final_amount))