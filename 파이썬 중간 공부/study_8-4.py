aa = "<<<파<<이>>썬>>>"
bb = ""

for i in range(0, len(aa)):
    if aa[i] != '<' and aa[i] != '>':
        bb += aa[i]
    
print("원래: "+aa)
print("이후: "+bb)