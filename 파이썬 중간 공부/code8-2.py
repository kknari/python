instr, outstr = "", ""

instr = input("문자열 입력: ")
ssinstr = len(instr)

for i in range(0, ssinstr):
    outstr += instr[ssinstr-(i+1)]

print(outstr)