x,y,z,num=0,50,0,0
for i in range(830000,1000001):
    print(i,x)
    z=0
    y=i
    #print(y,'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
        #print(y)
    while y!=1:
        if y%2==0:
            y=y//2
            z+=1
        else:
            y=3*y+1
            z+=1
            #print(z)
            if z>x:
                print(y)
                x=z
                num=i
print('the num:',num)

####################### 837799