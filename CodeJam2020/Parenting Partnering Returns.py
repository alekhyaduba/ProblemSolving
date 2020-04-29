numTCs = int(input())
result = []
timeList = []
for i in range(numTCs):
    assignment = []
    numActivity = int(input())
    activities = []
    flagImpossible = 0
    jEnd = 0
    cEnd = 0
    for a in range(numActivity):
        temp = ([int(act) for act in input().split()],a)
        activities.append(temp)
    activities.sort()

    for act in activities:
        if (act[0][0] >= jEnd ):
            assignment.append(("J",act[1]))
            jStart = act[0][0]
            jEnd = act[0][1]
        elif (act[0][0] >= cEnd):
            assignment.append(("C",act[1]))
            cStart = act[0][0]
            cEnd = act[0][1]
        else:
            flagImpossible = 1
            break

    if (flagImpossible):
        print("Case #" + str(i + 1) + ": IMPOSSIBLE")
    else:
        assignment.sort(key=lambda h:h[1])
        str_print = ''.join([x[0] for x in assignment])
        print("Case #" + str(i + 1) + ": " + str_print)
