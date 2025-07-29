k = int(input('nhap k nguyen, k > 0: '))
while k <= 0:
    print('loi nhap, lai \n')
    k = int(input('nhap k nguyen, k > 0: '))
    if k > 0: 
        break
a = list(range(k))
for i in range(len(a)):
    a[i] = int(input('a[' + str(i) +  '] = ') )
for i in range(len(a)):
    print(a[i], sep = " ", end = " ")
print("\n")
n = int(input('nhap so dong n, n > 1: '))
m = int(input('nhap so cot m, m > 1: '))
if n * m > k: print('NO')
else:
    b = [[0]*m for _ in range(n)]
    x = 0
    for i in range(n):
        for j in range(m):
            b[i][j] = a[x]
            x += 1
    for i in range(n):
        for j in range(m):
            print(b[i][j], sep = " ", end = " ")
        print()
    print("\n")
