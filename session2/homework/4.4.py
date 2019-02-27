# a
for i in range(20):
    print("* ",end="")


# b
n = int(input("Insert n: "))
for i in range(n):
    print("* ", end="")


# c
for i in range(4):
    print("x * ", end="")
print("x")


# d
n = int(input("Insert n: "))
if n%2 == 0:
    for i in range(int(n/2)):
        print("x * ", end="")
else:
    for i in range(int(n/2)):
        print("x * ", end="")
    print("x")


# e
print()

# f
for i in range(3):
    print()
    for i in range(7):
        print("* ", end="")


# g
m = int(input("Please insert row number: "))
n = int(input("Please insert column number: "))
for i in range(n):
    print()
    for i in range(m):
        print("* ", end="")

