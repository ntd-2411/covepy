n = int(input('nhap so phan tu cua mang: '))
while n <= 0: 
    print('loi nhap, lai')
    n = int(input('nhap so phan tu cua mang: '))
    if n > 0: 
        break

m = int(input('nhap so phan tu cua tap can xet: '))    
while n < 0: 
    print('loi nhap, lai')
    n = int(input('nhap so phan tu cua mang: '))
    if n == 0: 
        print('muc do hanh phuc khong doi')
        break
    elif n > 0: break

print(n, m, sep= " ")

list1 = []
for i in range(n):
    print('list[', i,'] = ', sep= '', end= '')
    x = int(input())
    list1.append(x)
print('mang vua nhap: ', list1)

b = set()
print('nhap set1: ')
for i in range(m):
    print('set[', i,'] = ', sep= '', end= '')
    x = int(input())
    b.add(x)
print('set1: ', b)
list2 = list(b)

c = set()
print('nhap set2: ')
for i in range(m):
    print('set[', i,'] = ', sep= '', end= '')
    x = int(input())
    c.add(x)
print('set2: ', c)
list3 = list(c)

dem = 0
for i in range(n):
    for j in range(m):
        if list1[i] == list2[j]: dem += 1
        elif list1[i] == list3[j]: dem -= 1

print('muc do hanh phuc: ', dem)