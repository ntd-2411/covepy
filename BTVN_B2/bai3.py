n = input('nhap chu so N: ')
dem = 0
tong = 0
a = list(n)
for i in range(len(a)):
    dem += 1
    tong += int(a[i])
print('N co ', dem, ' chu so')
print('tong cua chung = ', tong)
