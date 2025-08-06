n = int(input('nhap so luong so nguyen muon nhap: '))
while n <= 0: 
    print('loi nhap, lai \n')
    n = int(input('nhap lai: '))
list1 = []
for i in range(n):
    print('tuple(', i, '): ',sep= " ", end= ' ')
    x = int(input())
    list1.append(x)
tuple1 = tuple(list1)
print(tuple1)

tuple2 = ()
list2 = []
for i in range(n):
    if tuple1[i] % 5 == 0 and tuple1[i] % 10 != 0: list2.append(tuple1[i])
tuple2 = tuple(list1)
print(tuple2)

