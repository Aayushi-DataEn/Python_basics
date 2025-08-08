score = 185

if score >= 101:
    print("Please verify your grade again")
    exit()

if score < 60:
    grade = "A"

elif score < 70:
    grade = "D"

elif score < 80:
    grade = "C"

elif score < 90:
    grade = "B"

else:
    grade = "A"

print("Grade:", grade)