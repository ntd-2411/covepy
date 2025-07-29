# In ra chuỗi s3 là chuỗi s1 sau khi xóa các kí tự vị trí chẵn.
# Trả về chuỗi s4 là đan xen các kí tự của s1 và s2.
# VD: s1 = “abc”, s2 = “123” -> s4 = “a1b2c3”.
#1
s1 = input('nhap chuoi s1: ')
s2 = input('nhap chuoi s2: ')

#2
# '': sep chuoi sau khi dao; join: noi cac ki tu thanh chuoi moi; reversed(): tra ve 1 interator dao nguoc chuoi
s1 = ''.join(reversed(s1))
print('s1 sau dao nguoc: ' + s1)

#3
a = int(input('nhap a nguyen, a > 0: '))
b = int(input('nhap b nguyen, b > 0: '))
while (a < 1 or a >= b or a > len(s2)) or (b < 1 or a >= b or b > len(s2)):
    print('loi nhap, lai \n')
    a = int(input('nhap a nguyen, a > 0: '))
    b = int(input('nhap b nguyen, b > 0: '))
    if (a >= 1 or a < b or a <= len(s2)) or (b < 1 or a >= b or b > len(s2)): 
        break

x = list(s2)
i = a -1 
j = b - 1
while i < j:
    x[i], x[j] = x[j], x[i]
    i += 1
    j -= 1
s2 = ''.join(x)
print('s2 sau khi dao nguoc: ' + s2)

#4
y = list(s1)
# for ch in s1: duyet qua tung ki tu ch trong s1
# ch.isdigit(): ktra co phai la so khong
# int(ch) % 2 == 0: so do co la so chan khong
y = [char for char in s1 if not (char.isdigit() and int(char) % 2 == 0)]
s1 = ''.join(y)
print('s1 sau khi xoa phan tu chan: ' + s1)

#5
s4 = ""
min_len = min(len(s1), len(s2))
for i in range(min_len):
    s4 += s1[i] + s2[i]

s4 += s1[min_len:] + s2[min_len:]
print('s4 sau khi gop: ' + s4)
