# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []

    for index in range(len(prices)):
        product_revenue = prices[index] * quantities_sold[index]
        revenue.append(product_revenue)
    return revenue

revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products, revenue))
revenue_per_product = sorted(revenue_per_product)

print(revenue_per_product)

for product in revenue_per_product:
    product_name = product[0]
    product_revenue = product[1]
    
# Example of expected output line (do not remove):
    print(f"{product_name} has total revenue of ${product_revenue}")