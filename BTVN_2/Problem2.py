n = int(input('\n\tNhap so nguyen duong n: '))
if n <= 1:
    print('\n\tKhong co phan tu thoa man yeu cau\n')
else:
    dem2 = 0
    for i in range(2, n):
        dem1 = 0
        for j in range(1, n + 1):
            if i  % j == 0:
                dem1 += 1
        if dem1 % 2 != 0:
            dem2 += 1

print('\n\tCo ', dem2, ' phan tu co so uoc le thuoc tap (1, n)')