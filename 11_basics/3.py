# Task
# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.

# No rounding or formatting is necessary.


a = int(input())
b = int(input())
def floor_division(a, b):
    return a // b
def float(a,b):
    return a /b
print(floor_division(a, b))
print(float(a,b))        