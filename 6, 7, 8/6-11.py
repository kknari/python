for i in range(3, 101):
    for k in range(2, i):
        result = i%k

        if result==0:
            break

        if k==(i-1):
            print("%d " %i, end=' ')
