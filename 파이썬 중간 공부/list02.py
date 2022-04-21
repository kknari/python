zen =['Beautiful is better than ugly.'
'Explicit is better than implicit.'
'Simple is better than complex.']

sszen = len(zen)
count = 0

for data in zen:
    for index in range(len(data)):
        if data[index] == 'e':
            count += 1

print(count)