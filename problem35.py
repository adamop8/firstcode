y=0
h=0
a=[]
z=int(input('choose top number'))
for n in range(2, 101):
    for x in range(2, n):
        if n % x == 0:

                ##print(n, 'equals', x, '*', n//x)
             break
    else:
        #print(n, 'is a prime number')
        a=str(h)
        y+=1
        h=str(n)
        j=len(h)
        if j==2:
            r = h[0]
            t = h[1]
            q = t + r
            q=int(q)
            a=str(a)
            print(q,a)
            if q==a:
                print('hi')