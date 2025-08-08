input_str = "aayushi"


for chars in input_str:
    print(chars)
    if input_str.count(chars) == 1:
        print("Character is:", chars)
        break