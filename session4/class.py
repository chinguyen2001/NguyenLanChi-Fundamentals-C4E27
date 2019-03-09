# # Cấu trúc dữ liệu + thuật toán = Chương trình

# # List = liên tiếp nhau 

# colors = ["red", "green", "blue"]
# # b = colors

# # b[0]="yellow"
# # print(colors[0])

# # colors.insert(1,"cyan")
# # colors[1] = "cyan"

# # del colors[5]
# # colors.pop(1)
# # colors.remove("blue")

# # colors.reverse()
# # print(colors)

# print(colors)


# import random
# danh_sach_so = []
# n = int(input("Mời nhập n: "))
# for i in range(n):
#     print("Mời nhập số thứ {0} của bạn: ".format(i+1),end="")
#     so = int(input(""))
#     danh_sach_so.append(so)
# print("Danh sách các số của bạn là",danh_sach_so)

# a = int(random.choice(danh_sach_so))
# b = int(random.choice(danh_sach_so))

# while not a == b:
#     tong_hai_so = int(a + b)
#     if tong_hai_so%2 == 0:
#         print("Cặp số",a,"và",b,"của bạn có tổng là số chẵn.")
#     else:
#         print("Bạn không có cặp nào chia hết cho 2.")

# m = 3
# n = 4
# ds = [1,3,7]
# for i in range(m):
#     for j in range(i+1,n):  
#         print("i =",i,"; j =",j,"; Cặp là",ds[i],"  ",ds[j])
#         if (ds[i]+ds[j])%2 == 0:
#             print("Cặp số cần tìm là ",ds[i]," ",ds[j])


# Tìm bộ ba số x, y, z: 0 <= x,y,z <= 100
# sao cho x*2 + y*2 + z*2 = xyz

# danhsach = range(101)

# for i in range(101):
#     for j in range(i+1,101):
#         for l in range (j+1,101):
#             if i*2+j*2+l*2 == i*j*l:
#                 print("Bộ 3 số cần tìm là ({0},{1},{2})".format(i,j,l))


# person = [
#     {'name': 'Nguyễn Văn A', 'age': 21, 'address:': 'Hà Nội'},
#     {'name': 'Nguyễn Văn B', 'age': 22, 'address': 'HCM'}]

# print(person[1]['name'])


# dic = {}
# dic = dict()
# dic = {'name':'Nguyễn Văn A'}
# dic['age'] = 29
# dic['add'] = 'Hà Nội'
# age = dic['age']
# print(age)


# person = {'name':'Nguyễn Lan Chi', 'age': 18}
# person['SĐT'] = '0914960106' 
# # addr = person.get('address','Hà Nội')
# print(str(person))

# dic = {'computer':'máy tính', 'mouse':'chuột', 'keyboard':'bàn phím'}

# while True:
#     n = input("Mời nhập từ bạn muốn tra cứu: ")
#     if n in dic:
#         print(dic[n])
#     elif n == 'quit' or 'exit':
#         print("Bạn đã thoát ứng dụng.")
#         break
#     else:
#         print("Từ bạn tra không có trong từ điển.")




# n = str(input("Mời nhập từ bạn muốn tra cứu: "))

# if n in dictionary:
#     print(n['meaning'])
# elif n == 'exit' and 'quit':
#     print("Bạn đã thoát khỏi ứng dụng tra cứu.")
# else: 
#     print("Từ này không có trong từ điển tra cứu.")


# dic = {'computer':'máy tính', 'mouse':'chuột', 'keyboard':'bàn phím'}
# ra gia tri 
# for v in dic:
#     print(v)

# ra cap gia tri
# for k,v in dic.items():
#     print(k,":",v)

# ra gia tri
# for v in dic.values():
#     print(v)



dshocsinh = []
hs1 = {
    'name': 'Nguyen Lan Chi',
    'age' : '18',
    'add': 'Ha Noi',
    'SDT': ['0914','960106']
}
dshocsinh.append(hs1)
hs2 = {
    'name': 'Nguyen Minh Ha',
    'age' : '17',
    'add': 'Hai Phong',
    'SDT': ['0913','3333333']
}
dshocsinh.append(hs2)
# print(dshocsinh[0]['age'])
for v in dshocsinh:
    print(v['SDT'])



