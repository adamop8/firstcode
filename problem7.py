y=0
while 1==1:
    for n in range(2, 100000000):
        for x in range(2, n):
            if n % x == 0:

                #print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
           # print(n, 'is a prime number')
            y+=1
            if y==10001:
                print(n)
                exit(n)
##################################################### 104743



