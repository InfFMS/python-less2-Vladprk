x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
if x2 < x3 or x4 < x1:
    print('пустое множество')
elif x2 == x3:
    print(x2)
elif x1 == x4:
    print(x1)
else:
    if x2 > x3:
        print(x3, x2)
    elif x1 < x4:
        print(x1, x4)
