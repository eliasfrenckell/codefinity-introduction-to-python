# List of product prices
def apply_discount(prices):
    prices_copy = prices.copy()
    
    #prices_copy.append
    for index in range(len(prices_copy)):
        if prices_copy[index] > 2.00:
            prices_copy[index] *= 0.9
    
    return prices_copy

product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]
updated_price = apply_discount(product_prices)
#updated_prices = updated_prices * (1 - prices_copy[l])


print(f"Updated product prices: ${updated_price}")

# Call the function and store the updated prices
#updated_prices = apply_discount(product_prices)