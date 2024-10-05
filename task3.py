a = int(input())
if a%10 == 1:
    print(a, 'год')
elif a%10 >= 2 and a%10 <= 4:
    print(a, 'года')
else:
    print(a, 'лет')
