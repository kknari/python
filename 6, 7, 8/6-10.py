
i, k, starnum = 0, 0, 0
numstr, ch, starstr = "", "", ""


if __name__ == "__main__":
    numstr = input("숫자를 여러 개 입력하세요: ")
    print("")
    i = 0
    ch = numstr[i]
    while True:
        starnum = int(ch)

        starstr = ""
        for k in range(0, starnum*2):
            starstr += "\u2605"
            k += 1

        print(starstr)

        i += 1
        if (i>len(numstr)-1):
            break

        ch = numstr[i]