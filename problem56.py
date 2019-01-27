x,t,y,z='',0,0,0
for a in range(1,101):
    for b in range(1,101):
        #print(a,b,x)
        x=str(a**b)
        t=0
        y=0
        for s in x:
            #print(s)

                #print(x,'len',len(x),t,s)
                y+=int(s)

                t += 1
        if y>z:
            #print(y,z,x)
            z=y
            d=[x,a,b]


print(z,d)

########################  972