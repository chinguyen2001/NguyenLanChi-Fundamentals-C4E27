# Boolean là kiểu dữ liệu chỉ cho 2 giá trị là True và False

a = 24
b = 25

print("Với a =", a, "và b =", b)
print("a = b", a == b)
print("a > b", a > b)
print("a < b", a < b)



# Nested conditionals: là những điều kiện được lồng vào nhau 


x = input("Bạn tên là: ")
y = input("Người yêu bạn tên là: ")
if x == y:
    print ("Hai người hợp nhau đó ^^")
else:
    if x > y:
        print ("Hai bạn không hợp nhau rồi.")
    else:
        print ("Hai bạn còn hơn cả tri kỉ nữa.")