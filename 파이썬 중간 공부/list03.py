zen =['Beautiful is better than ugly.'
'Explicit is better than implicit.'
'Simple is better than complex.']

count = 0

for data in zen:
    for index in range(len(data)):
        print("%d " %index + data[index], end=' ')
        if data[index] == 'e':
            count += 1
            print("%d번째" %count)
        print("")

print("e 빈도수: %d" %count)
print("총 문자수: %d" %(len(data)-1))