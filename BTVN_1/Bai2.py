import re
s = input('Nhap vao chuoi ky tu: ')
s1 = 'hit'
s2 = 'HIT'
a = '16'
if(re.match(s, s1)):
    print('True')
elif(re.match(s, s2)):
    print('True')
else:
    print('Chuoi vua nhap khong xuat hien hit or HIT')
if(not re.match(a, s)):
    print('True')
else:
    print('Chuoi vua nhap co chu so 16')
