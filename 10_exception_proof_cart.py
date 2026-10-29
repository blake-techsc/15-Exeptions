prices = []

while True:
    try:
        user_input = input("Enter item price (Q to quit): ")
        if user_input.upper() == 'Q':
            raise KeyboardInterrupt
        price = float(user_input)
        if price < 0:
            print("Invalid price!")
        else:
            prices.append(price)
            print("Item added!")
    except ValueError:
        print("Invalid price!")
    finally:
        print("Entry processed.")

numItems = len(prices)
totalCost = sum(prices)

print(f"\nItems purchased: {numItems}")
print(f"Total: ${totalCost:.2f}")