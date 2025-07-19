x, y = map(int, input('lan luot nhap thang, nam: ').split())
print('thang vua nhap: ', x)
print('nam vua nhap: ', y)
if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
    print("trong nam ", y, " thang ", x, ' co 31 ngay')
elif x == 4 or x == 6 or x == 9 or x == 11:
    print("trong nam ", y, " thang ", x, ' co 31 ngay')
else:
    if(y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
        print("trong nam ", y, " thang ", x, ' co 29 ngay')
    else:
        print("trong nam ", y, " thang ", x, ' co 28 ngay')
