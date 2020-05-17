def print_rangoli(size):
    # your code goes here
    # width= n*4-3
    width=(size*4)-3
    a='a'
    list=[]
    for i in range(0,size):
        list.append(a)
        a=chr(ord(a) + 1)
    list.reverse()
    ##upper triangle
    for i in range(0,len(list)):
        print(list[i].center(width,'-'))


if __name__ == '__main__':
    print('e'.rjust(4,"-"),'-','e'.ljust(4, "-"),sep='')
    print('e'.ljust(4, "-"))
    print('e'.center(5, "-"))
    n = int(input())
    print_rangoli(n)
