# count = 1
# while count <=3:
#     print("Count is: ", count)
#     count += 1

# fruits = ["apple", "banana", "mango"]
# for i in fruits:
#     print(i)

# for i in range(1, 5):
#     print("Count is: ", i)

# for i in range(2):
#     for j in range(3):
#         print(i, j)

# i = 1
# while i <=2:
#     i += 1
#     j = 1
#     while j <= 3:
#         j += 1
#         print(f"i={i}, j={j}")


# numbers = [1, 3, 5, 7, 9]
# for num in numbers:
#     if num == 5:
#         print("Number 5 found, stopping the loop.")
#         break
#     print("Count is: ", num)


# for i in range(5):
#     if i == 2:
#         continue
#     print(i)



# marks = 105

# if marks >= 100:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# else:
#     print("Grade: C")



# age = 14
# has_id = True

# if age >= 18 or has_id:
#     print("Allowed!")
# else:
#     print("Not Allowed!")


# def greet(name):
#     print("Hello", name)

# greet("Aayushi")

# def add(a, b):
#     print("Sum is:", a+b)

# add(3, 5)


# def square(x, y):
#     return x ** y
# result = square(2, 3)
# print("Square is:", result)



# import math

# def circumference_circle(radius):
#     circle = 2 * math.pi * radius
#     return circle
# result = circumference_circle(4)
# print("Circumference of the circle is:", result)



# def add(a, b= 15):
#     return a + b
# print(add(5))
# print(add(3, 5))



# def greet(name = "Guest"):
#     print("Hello",name)

# greet()
# greet("Aayushi")


# x = 10
# def show():
#     print("Inside function is", x)

# show()
# print("Outside function is", x)
# y = 4
# def show():
#     y = 6
#     print("Inside function", y)

# show()
# print("Outside function is", y)



# def say_hello():
#     """This function says hello to the user."""
#     print("Hello!")



# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")

# for i in range(1, 11):
#     print(f"{int(a)} * {i} = {int(a) * i}")

# file = open('ravi.txt', 'w')

# with open('ravi.txt', 'w') as file:
#     file.write('Aayushi, keep focusing.\n')
#     file.write('Aayushi, do not irritate.\n')
#     file.write('Hey, how are you? \n')


# alphabet = "X"
# for i in range(1, 8):
#     print("X" * i)


# for i in range(1, 6):
#     print(" " * (5 - i) + "X" * i)
# Right Angled Triangle


n = 18

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 in range(2, 5):
    print("Not Weird")
elif n % 2 == 0 in range(6, 20):
    print("Weird")
elif n % 2 == 0 and  n > 20:
    print("Not Weird")