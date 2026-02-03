# task 1
name = input("Enter your name: ")
age = int(input("Enter your current age: "))

age_2030 = age+4

print(f"Hey {name}, you will be {age_2030} years old in 2030.")


# task 2
total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
share = total_bill / people 
print(f"Total Bill: {total_bill}")
print(f"Each person pays: {share}")
print(type(total_bill))
print(type(people))
print(type(share))


# task 3
item_name = "Laptop"
quantity = 2 
price = 499.99
in_stock = True
print("Item:", item_name,
      "Qty:", quantity,
      "Price:", price,
      "Available:", in_stock)
total_cost = quantity * price
print("Total Cost:", total_cost)