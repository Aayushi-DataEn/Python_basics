username = "chaiaurcode"

def func():
    username = "chai"
    print(username)


print(username)
func()


x = 98
# def func2(y):
#     z = x + y
#     return z

# result = func2(2)
# print(result)

# def func3():
#    global x
#    x = 12

# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()

def hellocoder(num):
    def actual(x):
        return x ** num
    return actual

f = hellocoder(2)
g = hellocoder(3)

print(f(3))
print(g(3))