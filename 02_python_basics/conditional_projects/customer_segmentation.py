# Mini Project: Customer Segmentation
# Concepts:
# - Nested conditionals
# - Business logic classification

purchase = int(input("Enter your total purchase: "))
frequency = int(input("How many times have you purchased?: "))

if purchase > 10000 and frequency > 10:
    print("Premium Customer")
elif purchase > 10000:
    print("High Value Customer")
elif frequency > 15:
    print("Loyal Customer")
else:
    print("Regular Customer")