ss='파이썬은완전재미있어요'

for i in range(0, len(ss)):
    if i%2!=0:
        print('#', end="")
    else:
        print(ss[i], end="")