dem = 0
x = 0
while True:
    x = int(input('nhap so tien ban co de mua bia: '))
    if x < 28: print('so tien ban co khong du de mua bia, moi nhap lai')
    else: break 
y = 28
while x >= y:
    dem += 1
    x -= 28
    if dem % 3 == 0: dem += 1
print('so tien ban co du de mua ', dem, ' chai bia')