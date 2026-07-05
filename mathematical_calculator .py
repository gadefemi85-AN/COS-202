print(" MATHEMATICAL CALCULATOR (MC)")
print("=========================")
while True:

    print("\nChoose an operation")
    print("+  : Addition")
    print("-  : Subtraction")
    print("*  : Multiplication")
    print("/  : Division")
    print("// : Integer Division")
    print("^  : Power")
    print("%  : Modulus")
    print("C  : Clear")
    print("OFF: Exit Calculator")

    choice = input("\nEnter your choice: ").upper()

    if choice == "OFF":
        print("Calculator Closed.")
        break

    elif choice == "C":
        print("\nScreen Cleared!")
        continue

    elif choice in ["+", "-", "*", "/", "//", "^", "%"]:

        value1 = float(input("Enter first value: "))
        value2 = float(input("Enter second value: "))

        if choice == "+":
            answer = value1 + value2

        elif choice == "-":
            answer = value1 - value2

        elif choice == "*":
            answer = value1 * value2

        elif choice == "/":
            if value2 != 0:
                answer = value1 / value2
            else:
                print("Error! Cannot divide by zero.")
                continue

        elif choice == "//":
            if value2 != 0:
                answer = value1 // value2
            else:
                print("Error! Cannot divide by zero.")
                continue

        elif choice == "^":
            answer = value1 ** value2

        elif choice == "%":
            if value2 != 0:
                answer = value1 % value2
            else:
                print("Error! Cannot divide by zero.")
                continue

        print("Answer =", answer)

    else:
        print("Invalid choice! Try again.")