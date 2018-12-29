##################################################################################################
#  A calculator containing all the operations of the account is rooting for the numbers entered  #
#                and showing the abbreviated multiplication formulas                             #
##################################################################################################
import math as z
x=int(input('enter a number as x '))
y=int(input('enter another number as y '))
print('x =',x)
print('y =',y)
print('root x=',z.sqrt(x))
print('root y=',z.sqrt(y))
print(' ')
print(x,'+',y,'=',x+y)
print(x,'-',y,'=',x-y)
print(x,'x',y,'=',x*y)
print(x,':',y,'=',x/y)
print('(x+y)(x-y):'),print('x*x-y*y =',x,'*',x,'-',y,'*',y,'=',x*x-y*y)
print(' ')
print('(x+y)**2:'),print('x*x+2xy+y*y =',x,'*',x,'+',2,'*',x,'*',y,'+',y,'*',y,'=',(x+y)**2)
print(' ')
print('(x-y)**2:'),print('x*x-2xy+y*y =',x,'*',x,'-',2,'*',x,'*',y,'+',y,'*',y,'=',(x-y)**2)
