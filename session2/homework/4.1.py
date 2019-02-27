x = int(input("Your height in cm is: "))
y = int(input("Your weight in kg is: "))
z = x/100
print("Your height in m is: ", z)

BMI = y/z**2
print("Your BMI is: ", BMI)

if BMI < 16:
    print("You are severely underweight.")
elif BMI > 30:
    print("You are obese.")
else:
    if 16 <= BMI < 18.5:
        print("You are underweight.")
    elif 18.5 <= BMI < 25:
        print("You are normal.")
    else:
        print("You are overweight.")