try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Enter a valid integer")