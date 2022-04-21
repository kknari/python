zen = 'Beautiful is better than ugly.'

sszen = len(zen)
count = 0

for i in range(0, sszen):
    if zen[i] == 'e' or zen[i] == 'E':
        count += 1

print(count)