import math as m
x,y=0,0
for i in range(134217728,1000000000001):
    for n in range (1,101):
        for e in range(1,101):
            if n**e>i:
                break
                if n**e!=i:
            #print(n,e)
                    break
                if len(str(i))==e:
                    print(i,'biggggggggggggggg')
                    x+=1
                    #exit(0)



print(x)