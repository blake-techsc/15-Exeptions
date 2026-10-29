animals = ["Dog", "Cat", "Rabbit", "Duck", "Horse"]

try:
    index = int(input("Enter an index: "))
    print(f"Animal at index {index}: {animals[index]}")
except ValueError:
    print("Enter a valid integer")
except IndexError:
    print("Index does not exist")