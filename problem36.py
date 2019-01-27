x,y=0,0
for p in range(1,1000001):
    if str(p)==str(p)[::-1]:
            #print(bin(p))
            b=str(bin(p))[2:]
            if b==b[::-1]:
                y+=1
                print(y,'.','num:',p,'binar:',bin(p))
                x+=p
print('sum:',x)

#########################  872187