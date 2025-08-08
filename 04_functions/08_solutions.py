def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")
print_kwargs(name="shaktiman")


# **kwargs is a type of DICTIONARY which allows many named inputs