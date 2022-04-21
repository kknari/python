aa = []
hap = 0

for i in range(0, 10):
    aa.append(0)

for k in range(0, 10):
    aa[k] = int(input(str(k+1)+"번째 숫자: "))
    
z=0
while z < 10:
    hap += aa[z]
    z += 1

print("합계: %d" %hap)
