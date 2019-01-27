x,y=0,0
for i in range(10,1000001):
    x=len(str(i))
    #print(x)
    #a,b,c,d,e,f,g,h=int(str(i)[0]),int(str(i)[1]),int(str(i)[2]),int(str(i)[3]),int(str(i)[4]),int(str(i)[5]),int(str(i)[6]),int(str(i)[7])
    if x==2:
        a, b= int(str(i)[0]), int(str(i)[1])
        if a**5+b**5==i:
            print(i,'okkkkkkkkkk')
            y+=i
    if x == 3:

        a, b, c = int(str(i)[0]), int(str(i)[1]), int(str(i)[2])
        if a**5+b**5+c**5==i :
                                                                
            y+= i
            print(i, 'okkkkkkkkkk')
    if x == 4:
        a, b, c, d = int(str(i)[0]), int(str(i)[1]), int(str(i)[2]), int(str(i)[3])
        if  a**5+b**5+c**5+d**5==i :
            y+= i
            print(i, 'okkkkkkkkkk')
    if x == 5:
        a, b, c, d, e= int(str(i)[0]), int(str(i)[1]), int(str(i)[2]), int(str(i)[3]), int(str(i)[4])
        if  a**5+b**5+c**5+d**5+e**5==i :
            y+= i
            print(i, 'okkkkkkkkkk')
    if x == 6:
        a, b, c, d, e, f= int(str(i)[0]), int(str(i)[1]), int(str(i)[2]), int(str(i)[3]), int(str(i)[4]), int(str(i)[5])
        if  a**5+b**5+c**5+d**5+e**5+f**5==i:
            y+= i
            print(i, 'okkkkkkkkkk')

    if x == 7:
        a, b, c, d, e, f, g, = int(str(i)[0]), int(str(i)[1]), int(str(i)[2]), int(str(i)[3]), int(str(i)[4]), int(str(i)[5]), int(str(i)[6])
        if  a**5+b**5+c**5+d**5+e**5+f**5+g**5==i :
            print(i, 'okkkkkkkkkk')
            y+= i

    if x == 8:
        a, b, c, d, e, f, g, h = int(str(i)[0]), int(str(i)[1]), int(str(i)[2]), int(str(i)[3]), int(str(i)[4]), int(str(i)[5]), int(str(i)[6]), int(str(i)[7])

        if a**5+b**5+c**5+d**5+e**5+f**5+g**5+h**5==i  :
            print(i, 'okkkkkkkkkk')
            y+= i

print(y)


#############################   443839