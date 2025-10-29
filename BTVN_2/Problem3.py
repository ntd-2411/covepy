n = int(input('\n\tNhap so luong hoc vien: '))
if n <= 0:
    print('\n\tLoi nhap, lai\n')
else:
    for i in range(n):
        name = input('\n\tNhap ho ten hoc vien: ')
        diem1 = float(input('\n\tNhap diem bai kiem tra thu 1: '))
        diem2 = float(input('\n\tNhap diem bai kiem tra thuong xuyen 2: '))
        if (diem1 + diem2) >= 200:
            hocLuc = 'Xuat Sac'
        elif (diem1 + diem2) >= 150 and (diem1 + diem2) < 200:
            hocLuc = 'Gioi'
        elif (diem1 + diem2) >= 100 and (diem1 + diem2) < 150:
            hocLuc = 'Kha'
        else:
            hocLuc = 'Yeu'

        print("\n\t", (i + 1), name, diem1 + diem2, hocLuc, sep = "_")