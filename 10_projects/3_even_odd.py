# numbers = [2, 3, 5, 6, 8, 55, 42, 85, 105, 75, 66, 91, 58, 14, 56, 74, 69, 89, 285, 1025]

# for i in numbers:
#     if i % 2 == 0:
#         print("Even Number:", i)
#     else:
#         print("Odd number:", i)



def numbers():
    try:
        num = int(input("Enter the number: "))
        if num % 2 == 0:
            print("The given number is an even number.")
        else:
            print("The given number is odd.")
        
        
    except ValueError:
        print("The given value is invalid")


numbers()


