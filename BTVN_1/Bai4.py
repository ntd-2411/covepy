n = int(input('Nhap so luong thanh vien HIT 16: '))

for i in range(n):
    name = input('Nhap ho ve ten: ')
    age = int(input('Nhap tuoi: '))
    sex = input('Nhap gioi tinh: ')
    mar = input('Nhap tinh trang hon nhan: ')

    print(name, age, sex, mar, sep = '_')
