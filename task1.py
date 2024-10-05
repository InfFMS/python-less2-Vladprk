a = int(input())
time1 = 510
if a == 3:
    print(f'Время начал урока - 10:20, Время конца урока - 11:05')
else:
    for i in range(a-1):
        time1 += 55
    time2 = time1 + 45
    print(f'Время начал урока - {time1//60}:{time1%60}, Время конца урока - {time2//60}:{time2%60}')
