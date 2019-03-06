sheep_sizes = [5,7,300,90,24,50,75]
print("Hello, I am the sheep keeper and here are the sizes of my sheep:")
print(sheep_sizes)

biggest_sheep = max(sheep_sizes)
print("Now my biggest sheep has size {0}. ".format(biggest_sheep),end="")
print("Let's shear it.")

sheared_sheep = int(sheep_sizes.index(biggest_sheep))
sheep_sizes.insert(sheared_sheep,8)
print("After shearing, here is my flock: ")
print(sheep_sizes)

one_month_flock = [n+50 for n in sheep_sizes]
print("One month has passed, now here is my flock: ")
print(one_month_flock)

two_month_flock = [n+50 for n in one_month_flock]
print("Two months have passed, now here is my flock: ")
print(two_month_flock)

biggest_sheep_2 = max(two_month_flock)
print("Now my biggest sheep has size {0}. ".format(biggest_sheep_2),end="")
print("Let's shear it.")
sheared_sheep_2 = int(two_month_flock.index(biggest_sheep_2))
two_month_flock.insert(sheared_sheep_2,8)
print("After shearing, here is my flock: ")
print(two_month_flock)

total_sizes = sum(two_month_flock)
total_income = int(total_sizes)*2
print("After two months, my flock has {0} size in total.".format(total_sizes))
print("Therefore, I would get {0} * 2$ = {1}$.".format(total_sizes,total_income))
