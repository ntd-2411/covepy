
n = int(input('nhap n nguyen, n > 0: '))
while n <= 0:
    print('loi nhap, lai \n')
    n = int(input('nhap n nguyen, n > 0: '))
    if n > 0: 
        break
a = list(range(n))
for i in range(len(a)):
    a[i] = int(input('a[' + str(i) +  '] = ') )
for i in range(len(a)):
    print(a[i], sep = " ", end = " ")
print("\n")

x = int(input('nhap x: '))
dem = 0
for i in range(len(a)):
    if a[i] == x:
        dem += 1
print(str(x) + ' xuat hien ' + str(dem) + ' lan trong list', sep = " ")
4, 0, 1, 3
for i in range(len(a)):
    if(i == 1): a[i] = 8
    elif(i == 2): a[i] = 5
    elif(i == 3): a[i] = 4
    elif(i == 4): a[i] = 0
    elif(i == 5): a[i] = 1
    elif(i == 6): a[i] = 3
for i in range(len(a)):
    print(a[i], sep = " ", end = " ")
print("\n")

max = a[0]
min = a[0]
for i in range(len(a)):
    if a[i] > max: max = a[i]

for i in range(len(a)):
    if a[i] < min: min = a[i]
print(str(max) + " la phan tu lon nhat trong list")
print(str(min) + " la phan tu nho nhat trong list")

y = int(input('nhap y: '))
a.insert(0,y)
for i in range(len(a)):
    print(a[i], sep = " ", end = " ")
print("\n")
temp1 = 0
temp2 = 0
for i in range(1, len(a)-1):
    if a[i-1] < a[i] and a[i] < a[i + 1]:
        temp1 += 1
if temp1 == len(a) - 2: print('list sap tang dan')
for i in range(1, len(a)-1):
    if a[i-1] > a[i] and a[i] > a[i + 1]:
        temp2 += 1
if temp2 == len(a) - 2: print('list sap giam dan')
if temp1 != len(a) - 2 and temp2 != len(a) - 2: print('NO')