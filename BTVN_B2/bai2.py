while True: 
    x = 0
    y = int(input('nhap thu nhap cua nhan vien muon check: '))
    print('check lai thong tin: ')
    print('thu nhap: ', y)
    if y > 15e6 or y == 15e6:
        x = 0.3
    elif y > 7e6 and y < 15e6:
        x = 0.2
    else: 
        x = 0.1
    print('thue thu nhap cua nhan vien do la: ', x*100, '%')
    print('luong rong nhan duoc sau thue: ', y - y*x ,"VND" )
    a = int(input('ban co muon kiem tra them thong tin? \n'\
    'co: nhap 1; khong: nhap 0 \n'))
    if a == 0:
        break
