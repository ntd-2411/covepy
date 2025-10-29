tongSoMon = 0
bill = 0.0

giuCho = input('\n\tNeu quy khach dang doi goi mon, vui long nhap pass: ')
goiMon = input('\n\tNeu quy khach bat dau goi mon, vui long nhap TIEP: ')

for i in range(100):
    print('\n\tNhap ten mon an thu ', (i + 1), ': ', end = '')
    name = input()
    cost = int(input('\n\tNhap gia tien mon an do: '))
    boMon = input('\n\tNeu quy khach muon bo mon nay, nhap BO: ')
    if boMon == 'BO':
        i -= 1
        continue
    else:
        tongSoMon += 1
        bill += cost
    stop = input('\n\tNeu khach hang da goi xong, nhap DUNG: ')
    if stop == 'DUNG':
        break

print('\n\tTong so mon: ', tongSoMon)
if bill > 200000:
    bill *= 0.9
print('\n\tSo tien khach hang can thanh toan: ', bill)
        


