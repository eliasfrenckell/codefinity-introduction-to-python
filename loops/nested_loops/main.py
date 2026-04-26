produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

print(groceries)

for section in groceries:
    for item in section:
        print(f"Item name: {item}")

'''for product in produce:
    for topping in dairy:
        print(product + " " + topping)
'''
