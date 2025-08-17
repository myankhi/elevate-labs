def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero!"
    return a % b

def percentage(a, b):
    return (a * b) / 100

def calculator():
    print("=== Simple CLI Calculator ===")
    while True:
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulo (%)")
        print("6. Percentage")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == "7":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice, try again!")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")
        elif choice == "5":
            print(f"Result: {modulo(num1, num2)}")
        elif choice == "6":
            print(f"Result: {percentage(num1, num2)} (i.e., {num2}% of {num1})")

if __name__ == "__main__":
    calculator()
