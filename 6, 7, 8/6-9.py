hap=0

for i in range(3333, 10000):
    if i%1234!=0:
        continue

    hap += i

print(hap)