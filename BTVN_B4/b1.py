n = int(input('nhap n: '))
while n <= 0:
    print('loi nhap, lai \n')
    n = int(input('nhap lai n: '))
    if n > 0: break
list1 = []
for i in range(n):
    print('tuple1(', i, ')', '=', sep = ' ', end = ' ')
    x = input()
    list1.append(x)
tuple1 = tuple(list1)
print('tuple1: ', tuple1)

list2 = []
for i in range(len(list1)):
    y = int(list1[i])
    list2.append(y)
tuple2 = tuple(list2)
print('tuple2: ', tuple2)


tong = 0
dem = 0
for i in range(len(list2)):
    tong += list2[i]
    dem += 1
print('tbc = ', 1.0*tong/dem)