import random
a,b,c=0,0,0
while 1==1:
    for a in range(1,1001):
        for b in range(1, 1001):
            c=1000-a-b

    #a=random.randint(100,500)
    #b=random.randint(100,500)
    #c=random.randint(100,500)
            print(a,b,c)
            if a+b+c==1000 and a**2+b**2==c**2:
                print('a:',a,'b:',b,'c:',c)
                print(a*b*c)
                exit(0)

    else:
        pass


   ###########
   # a: 200  #
   # b: 375  #
   # c: 425  #
   ###########    31875000
