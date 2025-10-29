s = input('\n\tNhap 1 chuoi ky tu can kiem tra: ')
value = False
for i in range(len(s)):
    for j in range(len(s) -1, -1, -1):
        if s[i] == '@' and s[j] == '.' and i + 1 < j:
            if i != 0 and i != len(s) - 1 and j != 0 and j != len(s) - 1:
                value = True
            
if value:
    print('\n\tVALID')
else:
    print('\n\tINVALID')
