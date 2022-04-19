hap=0

for i in range(3333, 10000):
    if not i%1234==0:
        continue

    else:
        hap += i

print(hap)