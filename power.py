

###############################   1

def power():
    y = int(input('enter a number for power '))
    z = int(input('enter a number for power with it '))
    a = y ** z
    print(a)
    return a
    power(y,z)

#########################   2

def powme(x):
    y=x**x
    print(y)
    return y

    powme(x)
############################  3
def powsum():
    x=0
    r=0
    y= int(input('enter a border  '))
    for i in range(1,y+1):
        y = i ** i
        r+=1
        print(r,'.',y)
        x+=y
    return x