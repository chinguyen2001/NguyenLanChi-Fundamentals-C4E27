# ---- Nhập n số từ bàn phím và tính tổng n số đó.
# n = int(input("Mời nhập n: "))
# tong = 0
# for i in range(n):
#     so = int(input("Nhập số: "))
#     tong = tong + so
# print("Tổng các số của bạn là", tong)

# age = 8
# if age < 10:
#     print("Baby")

# n = int(input("Mời nhập số của bạn: "))
# if n%2 == 0:
#     print("Số",n,"của bạn có chia hết cho 2.")

# age = int(input("Nhập số tuổi của bạn: "))
# if age <= 10:
#     print("You are a Baby.")
# elif age <= 16:
#     print("You are a Teen.")
# else:
#     print("You are an Adult.")


# yob = input("Nhập năm sinh của bạn: ")
# while not yob.isdigit():
#     print("Bạn đã nhập sai, vui lòng nhập lại!")
#     yob = input("Nhập năm sinh của bạn: ")

# age = 2019 - int(yob)
# print("Tuổi của bạn là", age)

# while 3 < 2:
#     print("Hi")


# password = input("Password: ")
# while len(password) < 8:
#     print("Bạn đã nhập sai, vui lòng nhập lại!")
#     password = (input("Password: "))
# print("Confirmed password.")

# password = input("Password: ")
# while True:
#     if len(password) >= 8:
#         break
#     print("Bạn đã nhập sai, vui lòng nhập lại!")
#     password = (input("Password: "))
# print("Confirmed password.")


# a = 1
# while True:
#     print("Loop count:",a)
#     # a-=1
#     # a = a + 1
#     a *= 2
#     if a >= 10:
#         break


# a = float(input("Please insert a: "))
# # while a == 0:
# #     print("a phải khác 0, vui lòng nhập lại!")
# #     a = float(input("Please insert a: "))
# b = float(input("Please insert b: "))
# c = float(input("Please insert c: "))

# if a == 0:
#     x = -c/b
#     print("Nghiệm của phương trình là {0}".format(x))
# else:
#     delta = int(b**2 - 4*a*c)
#     if delta < 0:
#         print("Phương trình vô nghiệm.")
#     elif delta == 0:
#         x = -b/(2*a)
#         print("Phương trình có nghiệm kép là {0}".format(x))
#     else:
#         x1 = (-b-delta**0.5)/(2*a)
#         x2 = (-b+delta**0.5)/(2*a)
#         print("Nghiệm của phương trình là {0} và {1}".format(x1,x2))

ls = []
n = int(input("Mời nhập n: "))
for i in range(n):
    print("Nhập phần tử thứ {0}: ".format(i+1),end="")
    so = int(input(""))
    ls.append(so)

print("Dãy bạn vừa nhập là ", end="")
print(ls)

print("Tổng dãy vừa nhập là", sum(ls))

# print("Phần tử thứ 2 trong dãy là ", end="")
# print(ls[1])

x = ls[len(ls)-1]
print(x)


