grocery_inventory = {
    
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

eggs = grocery_inventory.get("Eggs")
category, eggs_price, egg_stock = eggs

print("Eggs price is", eggs_price)

if eggs_price > 5:
        print("Eggs are too expensive, reducing the price by $1.")
        grocery_inventory["Eggs"] = (
            category,
            eggs_price - 1,
            egg_stock
        )
else:
        print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)


milk = grocery_inventory.get("Milk")
category, milk_price, milk_stock = milk

print("Milk stock is", milk_stock)

if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (
            category,
            milk_price,
            milk_stock + 20
        )
else:
    print("Milk has sufficient stock.")

apple = grocery_inventory.get("Apples")
#category, apple_price, apple_stock = apple
apple_price = apple[1]

if apple_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from the inventory due to high price.")


print("Updated inventory:", grocery_inventory)