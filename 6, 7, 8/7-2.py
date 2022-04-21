import random
n=[]

for _ in range(10):
    num = random.randrange(1, 100)
    n.append(_)

hap=0
for i in range(10):
    num = n[i]
    hap += num

print(hap)