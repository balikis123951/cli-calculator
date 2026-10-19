
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    history = []

    print("========== CLI CALCULATOR ==========")

    while True:
        print("\nChoose an operation:")
        print("+  Addition")
        print("-  Subtraction")
        print("*  Multiplication")
        print("/  Division")
        print("h  Calculation History")
        print("q  Quit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "q":
            print("Thank you for using the calculator. Goodbye!")
            break

        elif choice == "h":
            if not history:
                print("No calculations in history yet.")
            else:
                print("\n========== CALCULATION HISTORY ==========")
                for calculation in history:
                    print(calculation)
            continue

        elif choice not in ("+", "-", "*", "/"):
            print("Invalid choice. Please choose +, -, *, /, h, or q.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        if choice == "+":
            result = add(num1, num2)

        elif choice == "-":
            result = subtract(num1, num2)

        elif choice == "*":
            result = multiply(num1, num2)

        else:
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = divide(num1, num2)

        print("Result:", result)

        calculation = f"{num1} {choice} {num2} = {result}"
        history.append(calculation)


if __name__ == "__main__":
    main()
