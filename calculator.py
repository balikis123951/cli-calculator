def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def main():
    print("========== CLI CALCULATOR ==========")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1, num2)
            print("The sum is:", result)

        elif choice == "2":
            result = subtract(num1, num2)
            print("The difference is:", result)

        elif choice == "3":
            result = multiply(num1, num2)
            print("The product is:", result)

        elif choice == "4":
            result = divide(num1, num2)

            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print("The quotient is:", result)


if __name__ == "__main__":
    main()
