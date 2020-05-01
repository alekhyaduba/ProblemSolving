n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
a=[]
for _ in range(inputs):
    a.append([int(n) for n in input().split(" ")])
for x,y,incr in a:
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
max = x = 0
for i in list:
   x=x+i;
   if(max<x): max=x;
print(max)
"""
5 3
1 2 100
2 5 100
3 4 100
"""