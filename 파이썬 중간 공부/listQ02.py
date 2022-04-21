list1=[]
list2=[]
v=1

for i in range(0,3):
    for k in range(0,4):
        list1.append(v)
        v+=1
    list2.append(list1)
    list1=[]

for i in range(1,3):
    for k in range(2,4):
        print('%3d' %list2[i][k], end=' ')
    print(" ")