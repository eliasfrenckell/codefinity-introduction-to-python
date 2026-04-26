prices = [29.99, 45.50, 12.75, 38.20]

discount_factor = 0.10

for index in range(len(prices)):
    if index == 0:
        discount_factor = 0.10
    elif index == 1:
        discount_factor = 0.20
    elif index == 2:
        discount_factor = 0.15
    else:
        discount_factor = 0.05
        
    updated_price = prices[index] - (prices[index] * discount_factor)
    prices[index] = updated_price
    print(f"Updated price for item {index}: ${updated_price:.2f}")
