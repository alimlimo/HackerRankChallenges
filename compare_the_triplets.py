a=[17,28,30]
b=[99,16,8]


def compareTriplets(a,b) :
    c=[0,0]
    for i in range(0,3):
        if a[i] > b[i]:
            c[0] += 1
        elif a[i] < b[i]:
            c[1] += 1
    
    return c

c = compareTriplets(a, b)
print (c)