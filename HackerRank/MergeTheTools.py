def merge_the_tools(string, k):
    n=len(string)
    start=0
    end=k
    t_list=[]
    u_list=[]
    while end<=n:
        t_list.append(string[start:end])
        start=end
        end=end+k
    for t in t_list:
        temp=[]
        word=""
        for u in t:
            if u not in temp:
                word+=u
                temp.append(u)
        u_list.append(word)


    print(*u_list,sep="\n")

'''
ACDADAAAABBBCCA
5
'''

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
