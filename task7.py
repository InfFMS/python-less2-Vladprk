n = int(input())
for i in range(n):
    count = 0
    for x in range(1, n):
        if i%x == 0:
            count += 1
    if count == 2:
        print(i)
