
print("===== BASIC CALCULATOR =====")

while True:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("Result:", num1 + num2)

    if choice == "2":
        print("Result:", num1 - num2)

    if choice == "3":
        print("Result:", num1 * num2)

    if choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("Invalid choice!")