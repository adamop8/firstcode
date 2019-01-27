import random
x,y,z,a,b=100,100,' ','',0
while 100<=x<=999 and 100<=y<=999:
    a=x*y
    x=random.randint(900,999)
    y=random.randint(900,999)
    #print(x,' x ',y,'=')
    z=len(str(a))
    if z==6:
        if str(a)[0] == str(a)[5]:
            if str(a)[1] == str(a)[4]:
                if str(a)[2] == str(a)[3]:
                    print(a,'yes')

    else:
        pass
####################################  906609
