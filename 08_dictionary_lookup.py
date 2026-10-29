prices = {
    "pizza": 12,
    "burger": 8,
    "fries": 4,
    "soda": 2
}
    
print(f"Menu items: {', '.join(prices.keys())}")

try:
    item = input("Enter a food item: ").lower()
    price = prices[item]
    print(f"{item} costs ${price}.")
except KeyError:
    print("Item isn't on the menu")