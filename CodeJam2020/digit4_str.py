numCases = int(input())
setNumbers = []
result = []
for i in range(numCases):
    setNumbers.append((input()))

for number in setNumbers:
    a = ""
    b = ""
    for i in range(len(number)):
        if(number[i]=="4"):
            a=a+"3"
            b=b+"1"
        else:
            a=a+number[i]
            b=b+"0"


    result.append((a, b))

for i in range(len(result)):
    print("Case #" + str(i + 1) + ": " + str(result[i][0]) + " " + str(result[i][1]))