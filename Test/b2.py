s = input('nhap cac chuoi: ')
list1 = s.split()
set1 = set()
for item in list1: 
    for char in item:
        if char.isdigit(): set1.add(char)
        else: set1.add(char)
print(list(set1))



