n = int(input('nhap so luong sv đk bàn 1: '))
while n < 0: 
    print('loi nhap, lai \n')
    n = int(input('nhap lai: '))
    
m = int(input('nhap so luong sv dk ban 2: '))
while m < 0: 
    print('loi nhap, lai \n')
    m = int(input('nhap lai: '))

a = set()
for i in range(n):
    print('msv', i, ': ',sep= '', end= '')
    x = int(input())
    a.add(x)
print('set1: ', a)

b = set()
for i in range(m):
    print('msv', i, ': ',sep= '', end= '')
    x = int(input())
    b.add(x)
print('set2: ', b)

res = a.intersection(b)
if res != None: 
    print('co sv dk tai 2 ban: ', res)
else: print('khong co sv dk tai 2 ban')
res1 = a.difference(b)
if res1 != None:
    print('danh sach sv chi dk ban 1: ', res1)
else: print('tat ca sv deu dk 2 ban hoac chi dk ban 2')