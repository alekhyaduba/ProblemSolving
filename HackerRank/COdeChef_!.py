def weirdwalk(alice,bob):
    alice=[0]+alice
    bob=[0]+bob
    sum=0
    a_d=0
    b_d=0
    for i in range(len(alice)-1):
        a_d+=alice[i+1]
        b_d+=bob[i+1]
        a=alice[i+1]
        b=bob[i+1]

        if a==b and a_d==b_d:
            sum+=a


    return sum






tc= int(input())
result=[]
for i in range(tc):
    timesteps=int(input())
    alice=list(map(int,input().rstrip().split()))
    bob=list(map(int,input().rstrip().split()))
    result.append(weirdwalk(alice,bob))
print(*result,sep="\n")