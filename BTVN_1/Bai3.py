import string
import re
print('Chao mung den CLB Tin Hoc HIT')
s = 'CLB Tin Hoc HIT truc thuoc Truong CNTT - "10 diem"'
print(s)
for ch in s:
    if ch.isupper():
        print(ch, end = ' ')
print()
for ch in s:
    if not(ch.isupper()):
        print(ch, end = ' ')
print()
s1 = 'CLB Tin Hoc HIT truc thuoc Truong CNTT'
if re.match('CNTT', s1):
    print('YES')
else:
    print('NO')

s2 = ''
for ch in s1:
    if ch.isupper():
        s2 += ch.lower()
    elif not ch.isupper():
        s2 += ch.upper()
    else:
        s2 += ch
print('Chuoi sau khi thay doi: ', s2)



