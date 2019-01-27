x,y,t=0,0,0
for i in range(2,2000001):
    for n in range(2,i):
        if i%n==0:
            t+=1
            print(t)
            break
    else:
        t+=1
        x += i
        y += 1
        #print(y, 'prime:', i)
        print(t)


print('final:',x)