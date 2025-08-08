def basic_calculator():

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print('Choose operation: + - / *')
        operator = input("Enter operation: ")
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot be divided by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operations!")
            return
        
        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numbers.")


basic_calculator()
