e = 1
n = int(input('\n\tNhap so nguyen n: '))
x = float(input('\n\tNhap gia tri x: '))
if n == 0 or n > 10:
    print('\n\tLoi nhap, lai\n')
else:
    gt = 1
    for i in range(n):
        gt *= (i+1)
        e += pow(x,(i+1))/gt
print('\n\te^x = ', e)


s = 0
n = int(input('\n\tNhap so nguyen n: '))
if n == 0:
    print('\n\tLoi nhap, lai\n')
else:
    gt = 1
    for i in range(n):
        gt *= (i + 1)
        s += 1/gt
print('\n\tS = ', s)