def minion_game(string):
    vow=['A','E','I','O','U']
    con=[]
    kev=0
    stu=0
    size=len(string)

    alpha = 'A'
    for i in range(0, 26):
        if alpha not in vow:
           con.append(alpha)
        alpha = chr(ord(alpha) + 1)
    for j in range(0,len(string)):
        score=size-j
        if string[j] in vow:
            kev+=score
        else:
            stu+=score
    if kev>stu:
        print("Kevin "+ str(kev))
    elif stu>kev:
        print("Stuart "+ str(stu))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)