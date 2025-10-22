a, b = map(int, input('Lan luot nhap a, b: ').split())
print(a, ' + ', b, ' = ', a+b)
print(a, ' - ', b, ' = ', a-b)
print(a, ' * ', b, ' = ', a*b)
print(a, ' / ', b, ' = ', a//b)
print(a, '^', b, ' = ', pow(a, b))
print(a, '%', b, ' = ', a%b)
if a > b:
    print(a, ' > ', b)
elif a < b:
    print(a, ' < ', b)
else:
    print(a, ' = ', b)
if(a > 0 and b > 0):
    print('2 so vua nhap lon hon 0')
elif(a > 0 | b > 0):
    print('1 trong 2 so vua nhap lon hon 0')
print(a ^ b)
if not(a == b):
    print(a, ' != ', b)
else:
    print(a, ' = ', b)
print(a, 'dich phai 5 bit: ', a>>5)
print(a, ' dich trai 6 bit: ', a<<6)

