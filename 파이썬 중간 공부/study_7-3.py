aa=[]
bb=[]
value = 0

for i in range(0, 4):
    for k in range(0, 5):
        aa.append(value)
        value += 3
    bb.append(aa)
    aa = []

for i in range(0, 4):
    for k in range(0, 5):
        print("%d" % bb[i][k], end=" ")
    print("")