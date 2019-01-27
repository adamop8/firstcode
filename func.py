
# my moduls #





def power():   ###############################   1. power number with another one.
    y = int(input('enter a number for power '))
    z = int(input('enter a number for power with it '))
    a = y ** z
    print(a)
    return a
    power(y ,z)



def powme(x):   #########################   2. power a number by himself. y=x**x
    print(y)
    return y

    powme(x)



def powself():  ###########################  3. print and sum all to squere numbers up to x
    # +  print the digit lenght.

    x=0
    r=0
    z=''
    y= int(input('enter a border  '))
    for i in range(1,y+1 ) :
        y = i ** i
        r+=1
        print(r,'.' ,y)
        x+=y
    print('sum:',x)
    z=len (str(x))
    print('digit lenght:',z)

    return x



def palindrome(x):  ############################## 4. print all the palindrome numbers up to 'x'.
    y=''
    r=0
    for n in range(10,x+1 ) :
        y=str (n)
        if y == y[ : : -1]:
            r+= 1
            print(r,'. ',n)


# palindrome(10000)


def encrypter():  ##################### 5. slove and encrypt sentenses and words
    s = ""
    o = ""
    z = input('write sentese for encrypt ') + '   '
    y = 0
    # y=int(input('Select a number to move the letters and encrypt it '))
    for y in range(24):
        for x in z:
            if ord(x) >= ord('a') and ord(x) <= ord('z'):
                o += chr((ord(x) + y - ord('a')) % 26 + ord('a'))
            else:
                o += x
    print(o)
    print('   ')


def trinum(x):  ########################## 6. return list of all the triangle numbers up to x
    y = 0
    z = []
    for i in range(1, 31):
        for n in range(i, x + 1):
            y += n
            z.append(y)
            # print('..')
            # print(z)
    return x


def powsum():  ###########################  7. print and sum all the numbers in power of 2 up to x
    # +  print the digit lenght.

    x = 0
    r = 0
    z = ''
    y = int(input('enter a border  '))
    for i in range(1, y + 1):
        y = i ** 2
        r += 1
        print(r, '.', y)
        x += y
    print('sum:', x)
    z = len(str(x))
    print('digit lenght:', z)

    return x