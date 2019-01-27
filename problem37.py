x,y=0,''
while x!=11:
    for i in range(2,1000000001):
        for n in range(2,i):
            if i%n==0:
                break
        else:
            print(i)
            x=len(str(i))
            y=str(i)
            if x==2:
                for a in range(2, i):
                    if int(y[0])%a==0 and int(y[1])%a==0:
                        if int(y[0])%a==0 and int(y[1])%a==0:
                            if int(y[0])!=1 and int(y[1])!=1:
                                break
                        else:
                            print(i,'okkkkkkk')
