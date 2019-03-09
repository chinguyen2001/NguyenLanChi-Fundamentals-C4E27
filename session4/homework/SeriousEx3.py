print("Answer the following questions.")

print("What is the average length of a car?")
answers_1 = {
    'A': 170,
    'B': 175,
    'C': 177,
    'D': 180
}
for (k,v) in answers_1.items():
    print(k,"-",v)
ans1 = input("Your answer: ")
correctans = 0
if ans1 == 'C':
    print('Bingo!')
    correctans += 1
else:
    print("Wrong :'(")

print("What is the fear of cats called?")
answers_2 = {
    'A': 'Gatophobia',
    'B': 'Sociophobia',
    'C': 'Tropiphobia',
    'D': 'None'
}
for (a,b) in answers_2.items():
    print(a,"-",b)
ans2 = input("Your answer: ")
if ans2 == 'A':
    print('Bingo!')
    correctans += 1
else:
    print("Wrong :'(")

print("You have answered {0} out of 2 questions correctly.".format(correctans))