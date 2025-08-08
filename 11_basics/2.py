# TASK 1
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.



a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

def add(a, b):
    return a + b
def subtraction(a, b):
    return a - b 

def multiply(a, b):
    return a* b

print("The sum of two numbers:", add(a, b))
print("The difference of the two numbers:", subtraction(a, b))
print("The product of the two numbers:", multiply(a, b))






