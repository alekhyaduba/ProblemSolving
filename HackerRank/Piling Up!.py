import sys
def solve(seq,leng):
    curLen=sys.maxsize
    right=leng-1
    left=0
    possible=True
    i=0
    while i<=leng-1:
        if (seq[left]<=curLen) and (seq[right]<seq[left]):
            possible &= True
            curLen=seq[left]
            left+=1
        elif (seq[right]<=curLen) and(seq[left]<seq[right]):
            possible&= True
            curLen=seq[right]
            right-=1
        elif seq[left]==seq[right]:
            possible&=True
            curLen=seq[left]
            left+=1
        else:
            possible&=False
            break
        i+=1

    return "Yes" if possible else "No"


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        len = int(input())
        seq = list(map(int, input().rstrip().split()))

        result=solve(seq,len)
        print(result)
