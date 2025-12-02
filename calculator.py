from utils import clear_screen, pause

def calculator_menu():
    while True:
        clear_screen()
        print("=== Calculator ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "6":
            break

        try:
            num1 = float(input("Enter first number: ").strip())
            num2 = float(input("Enter second number: ").strip())
        except ValueError:
            print("Invalid number. Please enter numeric values.")
            pause()
            continue

        if choice == "1":
            result = num1 + num2
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero not allowed.")
                pause()
                continue
            result = num1 / num2
        elif choice == "5":
            result = num1 ** num2
        else:
            print("Invalid choice.")
            pause()
            continue

        print(f"\nResult = {result}")
        pause()