n = int(input('nhap so phan tu cua mang: '))
while n <= 0: 
    print('loi nhap, lai')
    n = int(input('nhap so phan tu cua mang: '))
    if n > 0: 
        break

a = []
for i in range(n):
    print('list[', i,'] = ', sep= '', end= '')
    x = input()
    a.append(x)
print('mang vua nhap: ', a)

b = tuple(a)
print('tuple b: ', b)

def check(s):
    for ch in s:
        if ch <'0' or ch > '9':
            return False
        else:
            return True

dem = 0
for i in range(len(b)):
    if check(b[i]): dem += 1

print('co ', dem, ' phan tu trong b dang so', sep= '')