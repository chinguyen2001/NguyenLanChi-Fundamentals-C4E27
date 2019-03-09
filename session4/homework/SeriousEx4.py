print("Answer the following questions.")

print("What is the debut year of boygroup band BTS?")
answers_1 = {
    1: 2010,
    2: 2012,
    3: 2013,
    4: 2016
}
for (k,v) in answers_1.items():
    print(k,"-",v)
ans1 = int(input("Your answer: "))
correctans = 0
if ans1 == 3:
    print('Bingo!')
    correctans += 1
else:
    print("Wrong :'(")
    
print("What is the production company behind the film Spirited Away?")
answers_2 = {
    1: 'Skywork',
    2: 'Ghibi',
    3: 'SteamProduction',
    4: 'Mangaholics'
}
for (a,b) in answers_2.items():
    print(a,"-",b)
ans2 = int(input("Your answer: "))
if ans2 == 2:
    print('Bingo!')
    correctans += 1
else:
    print("Wrong :'(")

print("You have answered {0} out of 2 questions correctly.".format(correctans))