x,y,z,a,b=0,0,0,' ',0
def lencheck(x):

    if b==1:
        int(a[0])
    elif b==2:
        int(a[0]+a[1]*x)
    elif b==3:
        int(a[0] + a[1] * x+a[2]*x**2)
    elif b==4:
        int(a[0] + a[1] * x + a[2] * x**2+a[3]*x**3)
    elif b==5:
        int(a[0] + a[1] *  + a[2] * x**2 + a[3] * x**3+a[4]*x**4)
    elif b==6:
        int(a[0] + a[1] * x + a[2] * x**2 + a[3] * x**3 + a[4] * x**4+a[5]*x**5)
    elif b==7:
        int(a[0] + a[1] * x + a[2] * x**2 + a[3] * x**3 + a[4] * x**4+a[5]*x**5+a[6]*x**6)
    elif b == 8:
        int(a[0] + a[1] * x + a[2] * x ** 2 + a[3] * x ** 3 + a[4] * x ** 4 + a[5] * x ** 5 + a[6] * x ** 6+a[7]*x**7)


x=str(input('do you want to change number or calculate sam of 2 numbers? [change/calculate] '))
if x=='change' :
   y=int(input('enter a number for change '))
   x=int(input('in what base the number? [2/8/10/16] '))
   z=int(input('for what base you want to change it? [2/8/10/16] '))
   if x==2 | x==8 | x==10 | x==16 :
       pass
   if x==3 :
       print('This base does not exist in the computer language')

   if x==10 :
       if z==2 :
        print(y,'in base 10(Decimal) =',bin(y),'in base 2(Binary)')
       if z==10 :
        print('this number already in base 10(Decimal)')
       if z==8 :
        print(y, 'in base 10(Decimal) =', oct(y), 'in base 8(Octal)')
       if z==16:
        print(y, 'in base 10(Decimal) =', hex(y), 'in base 16(Hexadecimal)')
   elif x==8 :
       if z==2 :
        y=oct(y)
        print(y, 'in base 8(Octal) =', bin(y), 'in base 2(Binary)')
       if z==10 :
           y = oct(y)
           print(y, 'in base 8(Octal) =',lencheck(), 'in base 10(decimal)')
       if z==8 :
        print('this number already in base 8(Octal)')
        exit(0)
       if z==16:
        y = oct(y)
   elif x==2 :

       if z==2 :
           print('this number already in base 2(binar)')
       if z==10 :
          y = bin(y)
       if z==8 :
          y = bin(y)
       if z==16:
          y = bin(y)
   elif x==16 :
        if z==2 :
            y=hex(y)
        if z==10 :
            y = hex(y)
        if z==8 :
            y = hex(y)
        if z==16:
            print("hi")





            ##############################################################################

            def lencheck():
                a, y, x, b = input('enter s number with his base form  [0b/0x/0o]  '), int(
                    input(' for what base you want to change it? [2/8/10/16]  ')), 0, 0
                b = len(a) - 2
                print(b)
                print(a)
                if b == 1:
                    x = int(a[0])
                elif b == 2:
                    x = int(a[0] + a[1] * x)
                elif b == 3:
                    x = int(a[0] + a[1] * x + a[2] * x ** 2)
                elif b == 4:
                    x = int(a[0] + a[1] * x + a[2] * x ** 2 + a[3] * x ** 3)
                elif b == 5:
                    x = int(a[0] + a[1] * x + a[2] * x ** 2 + a[3] * x ** 3 + a[4] * x ** 4)
                elif b == 6:
                    x = int(a[0] + a[1] * x + a[2] * x ** 2 + a[3] * x ** 3 + a[4] * x ** 4 + a[5] * x ** 5)
                elif b == 7:
                    x = int(
                        a[0] + a[1] * x + a[2] * x ** 2 + a[3] * x ** 3 + a[4] * x ** 4 + a[5] * x ** 5 + a[6] * x ** 6)
                elif b == 8:
                    x = int(a[0] + a[1] * x + a[2] * x ** 2 + a[3] * x ** 3 + a[4] * x ** 4 + a[5] * x ** 5 + a[
                        6] * x ** 6 + a[7] * x ** 7)
                print(x)


            lencheck()