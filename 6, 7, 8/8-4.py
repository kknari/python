inStr = 'IT_CookBook_Python'
outStr = ''

for i in range(0, len(inStr)):
    if i%2==0:
        outStr += inStr[len(inStr)-(i+1)]
    else:
        outStr += '#'
    
print(inStr)
print(outStr)

ss='Python'

for i in range(0, len(ss)):
    print(ss[i]+'$', end='')
print("\n")

str1 = '코딩 중에서 파이썬 코딩이 가장 즐거운 코딩'

print(str1.count('코딩'))
print(str1.rfind('코딩'))
print(str1.startswith('코딩'))
print(str1.find('파이썬'))

dd='Python 파이썬'
print(dd.replace('파이썬', 'Python'))