while True:
    d = int(input('\n\tNhap ngay: '))
    m = int(input('\n\tNhap thang: '))
    if d <= 0 or d > 31:
        print('\n\tLoi nhap, vui long nhap lai\n')
    elif m <= 0 or m > 12:
        print('\n\tLoi nhap, vui long nhap lai\n')
    else:
        if (m == 1 and d >= 20) or (m == 2 and d <= 18):
            print('\n\tBan thuoc cung bao binh')
        elif  (m == 3 and d >= 21) or (m == 4 and d <= 20):
            print('\n\tBan thuoc cung bach duong')
        elif  (m == 4 and d >= 21) or (m == 5 and d <= 20):
            print('\n\tBan thuoc cung kim nguu')
        elif  (m == 5 and d >= 21) or (m == 6 and d <= 21):
            print('\n\tBan thuoc cung song tu')
        elif  (m == 6 and d >= 22) or (m == 7 and d <= 22):
            print('\n\tBan thuoc cung cu giai')
        elif  (m == 7 and d >= 23) or (m == 8 and d <= 22):
            print('\n\tBan thuoc cung su tu')
        elif  (m == 10 and d >= 24) or (m == 11 and d <= 22):
            print('\n\tBan thuoc cung bo cap')
        elif  (m == 8 and d >= 23) or (m == 9 and d <= 22):
            print('\n\tBan thuoc cung xu nu')
        elif  (m == 9 and d >= 23) or (m == 10 and d <= 23):
            print('\n\tBan thuoc cung thien binh')
        elif  (m == 2 and d >= 19) or (m == 3 and d <= 20):
            print('\n\tBan thuoc cung song ngu')
        elif  (m == 11 and d >= 23) or (m == 12 and d <= 21):
            print('\n\tBan thuoc cung nhan ma')
        elif  (m == 12 and d >= 22) or (m == 1 and d <= 19):
            print('\n\tBan thuoc cung ma ket')
        
        s = input('\n\tBan co muon dung lai khong? Neu co an 0: ')
        if s == '0':
            break