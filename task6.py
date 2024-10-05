for i in range(99, 999):
    if (i%10)**3 + (i//10%10)**3 + (i//100)**3 == i:
        print(i)
