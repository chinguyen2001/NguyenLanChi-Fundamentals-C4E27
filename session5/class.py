# m = int(input("Nhập m: "))
# tong = 0
# for i in range(m):
#     print("Nhập số thứ {0}: ".format(i+1),end="")
#     sonhap = int(input(""))
#     tong = tong + sonhap
# print("Tổng các số của bạn là",tong)

# n = int(input("Nhập n: "))
# tong2 = 0
# for i in range(n):
#     print("Nhập số thứ {0}: ".format(i+1),end="")
#     sonhap2 = int(input(""))
#     tong2 = tong2 + sonhap2
# tbc = int(tong2)/n
# print("Trung bình cộng các số của bạn là",tbc)

# def function_name([parameters]):
#     ...
    
#     [return <>]

# Function không tham số
# def say_hi():
#     print("hi")
#     print('bye')

# say_hi()
# say_hi()
# say_hi()
# say_hi()
# say_hi()


# def add_two_number(a,b):
#     print("Tổng hai số là:",a+b)

# # num1 = int(input("Nhập số thứ nhất: "))
# # num2 = int(input("Nhập số thứ hai: "))
# add_two_number(4*3,6+3+5)


# def add_two_number(a,b):
#     print(a+b)
#     return a+b

# print(add_two_number(1,2)

# tính được >= 3 số
# phải nằm trong body của hàm
# sẽ trả về kết quả cho lời gọi hàm tong = add_two_number(1,2)

# num1 = int(input("Nhập số thứ nhất: "))
# num2 = int(input("Nhập số thứ hai: "))
# num3 = int(input("Nhập số thứ ba: "))
# sum12 = add_two_number(num1,num2)
# sum3 = add_two_number(sum12,num3)
# print("Tổng 3 số là",sum3)


# def abs_of_num(a):
#     if a > 0:
#         return a
#         print("Trị tuyệt đối là",a)
#     else:
#         return -a
#         print("Trị tuyệt đối là",-a)
#     print("Trị tuyệt đối là",a)

# x = abs_of_num(-12)
# tong = 12 + abs_of_num(-12)
# print(x)
# print(tong)

# def evaluate(a,b,c):
#     if c == '+':
#         return a + b 
#     elif c == '/':
#         return a / b
#     elif c == '*':
#         return a*b
#     elif c == '-':
#         return a-b

# print(evaluate(4,6,'*'))

def prime_numb(a):
    if a < 2:
        return False
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

n = int(input("Mời nhập n: "))
listprime = []
for v in range(0,n+1):
    if prime_numb(v):
        listprime.append(v)
print("Danh sách số nguyên tố bé hơn n là:",listprime)
