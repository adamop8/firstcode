#Shows the Fibonacci series up to the number the user has selected
x,y=0,1
z=int(input('enter a number'))
r=0
z=z-1
while r<=z:

        x,y=y,y+x
        r=r+1

print(r,'.',x)
