n = int(input('nhap so luong phan tu muon nhap(1<= n <=100): '))
while n < 1 or n > 100: 
    print('loi nhap, lai \n')
    n = int(input('nhap lai: '))
a = []

for i in range(n):
        print('a(', i, '): ',sep= " ", end= ' ')
        x = int(input())
        a.append(x)

print(a)

