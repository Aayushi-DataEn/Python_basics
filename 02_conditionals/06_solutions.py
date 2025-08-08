distance = 18

if distance < 3:
    transportation = "Walk"

elif distance < 16:
    transportation = "Bike"

else:
    transportation = "Car"

print("AI recommends you the transport of", transportation)