



def readInputMatrix():
    size = int(input())
    matrix = []
    for i in range(size):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    return matrix

def calculateTrace(matrix):
    trace=0
    for i in range(len(matrix)):
        trace=trace+ matrix[i][i]
    return trace
def calculateRowsWithRepeatation(matrix):
    r=0
    for i in range(len(matrix)):
        flag=[0 for l in range(len(matrix))]
        for j in range(len(matrix)):
            position=matrix[i][j]
            if(flag[position-1]==0):
                flag[position-1]=1
            else:
                flag[position-1]=0
        if 0 in flag:
            r=r+1
    return r

def calculateColumnsWithRepeatation(matrix):
    c=0
    for i in range(len(matrix)):
        flag=[0 for l in range(len(matrix))]
        for j in range(len(matrix)):
            position=matrix[j][i]
            if(flag[position-1]==0):
                flag[position-1]=1
            else:
                flag[position-1]=0

        if 0 in flag:
            c=c+1
    return c


numTCs=int(input())
for i in range(numTCs):
    matrix=readInputMatrix()
    result=[]
    result.append((calculateTrace(matrix)))
    result.append((calculateRowsWithRepeatation(matrix)))
    result.append((calculateColumnsWithRepeatation(matrix)))
    print("Case #"+str(i+1)+": "+str(result[0])+" "+str(result[1])+" "+str(result[2]))

