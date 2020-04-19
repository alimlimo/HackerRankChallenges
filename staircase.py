def staircase(n):
    for i in range(0,n+1):
        for z in range (0,n-i):
            print(" ",end='')
        for j in range(0,i):
            print("#",end='')
        print(" ")