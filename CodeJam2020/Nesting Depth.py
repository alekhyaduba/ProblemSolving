numTCs = int(input())
for i in range(numTCs):
    inStr = input() + "0"
    string = [int(inStr[x]) for x in range(len(inStr))]
    result = ""
    pO = 0
    pC = 0
    for item in string:
        diff = item - pO
        if diff >= 0:
            pO += diff
            for x in range(diff):
                result += "("
            result += str(item)

        else:
            pC += -diff
            pO = pO + diff
            for y in range(-diff):
                result += ")"
            result += str(item)

    print("Case #" + str(i + 1) + ": " + result[:-1])
