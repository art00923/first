def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def power(x, y):
    return x ** y

def mod(x, y):
    if y == 0:
        return "Error: Cannot modulo by zero."
    return x % y

def calculator():
    print("Simple Calculator")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Modulo (x % y)")
        print("0. Exit")

        choice = input("Enter choice (0/1/2/3/4/5/6): ")

        if choice == '0':
            print("Goodbye!")
            break
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid input. Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input. Please enter valid numbers.")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = power(num1, num2)
        elif choice == '6':
            result = mod(num1, num2)
        print("Result:", result)

if __name__ == "__main__":
    calculator()
