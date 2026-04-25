print("Shopping Receipt")
print("-----------------------")
item1 = 162*1.2
print("Item 1: $", item1)  # Price per weight
discounted_price = 25-3
print("Item 2: $", discounted_price)  # Discounted price
print("-----------------------")
Subtotal = item1 + discounted_price
print("Subtotal: $", Subtotal)
print("Tax (8%): $", Subtotal*0.08)
print("-----------------------")
print("Thank you for shopping!")