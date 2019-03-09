sen = input("Nhap day cua ban: ")

sen = sen.lower() 

alphabet = 'abcdefghijklmnopqrstuvwxyz'

danhsachchuso = {}
for a in sen:
    if a in alphabet:
        if a in danhsachchuso:
            danhsachchuso[a] = danhsachchuso[a] + 1
        else:
            danhsachchuso[a] = 1

keys = sorted(danhsachchuso.keys())

for a in keys:
    print(a, danhsachchuso[a])
