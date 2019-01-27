import sys as x
y = int(input('enter a number for power '))
z = int(input('enter a number for power with it '))
a=str(y**z)
b=len(a)
print(b)
if b<=3:
    print(y, 'in the power of', z, '=', a)
elif 4==b:
    print(y, 'in the power of', z, '=', a[0]+','+a[1:4])
elif b==5:
    print(y, 'in the power of', z, '=', a[:2] + ',' + a[2:5])
