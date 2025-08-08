def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1, 2))
print(sum_all(3, 4, 5, 6, 2))

# *args can solve multiple variables together and args is a type of TUPLE. Allows many unnamed inputs