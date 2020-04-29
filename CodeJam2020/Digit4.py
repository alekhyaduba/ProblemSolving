numCases = int(input())
setNumbers = []
result = []
for i in range(numCases):
    setNumbers.append(int((input())))

for number in setNumbers:
    a = number
    num = number
    b = 0
    i = 0
    while num != 0:
        if num % 10 == 4:
            a = a - pow(110, i)
            b = b + pow(10, i)
        num = int(num / 10)
        i = i + 1

    result.append((a, b))

for i in range(len(result)):
    print("Case #" + str(i + 1) + ": " + str(result[i][0]) + " " + str(result[i][1]))
