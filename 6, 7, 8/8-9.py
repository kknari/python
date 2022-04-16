ins, outs = "Python", ""
strlen = len(ins)

for i in range(0, strlen):
    outs += ins[strlen-(i+1)]

print(outs)

ss="IT_CookBook"
print('#'.join(ss))