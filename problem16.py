y,z=0,int(input('choose number to power with it  '))
x=str(2**z)
for i in x:
    i=eval(i)
    y=y+i

#print(len(str(x)),'hi')
    #print(i,'this i')
    #print(y)

print('the number:',x,'=','2**'+str(z))
print('the sum of the digits:',y)

############################   the sum: 1366