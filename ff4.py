import os


################ version[3.7.1] ############### version[3.7.1] ############### version[3.7.1] ############### version[3.7.1]

#the script gets 2 values of points and prints them and the slope.

#The script will not accept a value other than a number.

################ version[3.7.1] ############### version[3.7.1] ############### version[3.7.1] ############### version[3.7.1]



x1=input('please enter a point value of x: ')


while x1=='':
    print('You have not entered a value')
    x1 = input('please enter a point value of x: ')



if '.' in x1:
        while 'a' in x1 or 'b' in x1 or 'c' in x1 or 'd' in x1 or 'e' in x1 or 'f' in x1 or 'g' in x1 or 'h' in x1 or 'i' in x1 or 'j' in x1 or 'k' in x1 or 'l' in x1  or 'm' in x1 or 'n' in x1 or 'o' in x1 or 'p' in x1 or 'q' in x1 or 'r' in x1 or 's' in x1 or 't' in x1 or 'u' in x1 or 'v' in x1 or 'w' in x1 or 'x' in x1 or 'y' in x1 or 'z' in x1 or'A' in x1 or 'B' in x1 or 'C' in x1 or 'd' in x1 or 'E' in x1 or 'F' in x1 or 'G' in x1 or 'H' in x1 or 'I' in x1 or 'J' in x1 or 'K' in x1 or 'L' in x1  or 'M' in x1 or 'N' in x1 or 'O' in x1 or 'P' in x1 or 'Q' in x1 or 'R' in x1 or 'S' in x1 or 'T' in x1 or 'U' in x1 or 'V' in x1 or 'W' in x1 or 'X' in x1 or 'Y' in x1 or 'Z' in x1 or '/' in x1  or ';' in x1 or ':' in x1 or '!' in x1 or '@' in x1 or '#' in x1 or '$' in x1 or '%' in x1 or '^' in x1 or '&' in x1 or '*' in x1 or ')' in x1 or '(' in x1 or '<' in x1 or '>' in x1 or ',' in x1 or '`' in x1 or '~' in x1 or '+' in x1 or '=' in x1 or '_' in x1 or '?' in x1 or '[' in x1 or ']' in x1 or '{' in x1 or '}' in x1 or '|' in x1 or '"' in x1 or '\ ' in x1:

                print('enter a #NUMBER#')
                x1 = input('please enter a point value of x: ')
        else:
            if '.' in x1:
                r=float(x1)
            else:
                r=int(x1)
if '.' not in x1:
    while 'a' in x1 or 'b' in x1 or 'c' in x1 or 'd' in x1 or 'e' in x1 or 'f' in x1 or 'g' in x1 or 'h' in x1 or 'i' in x1 or 'j' in x1 or 'k' in x1 or 'l' in x1  or 'm' in x1 or 'n' in x1 or 'o' in x1 or 'p' in x1 or 'q' in x1 or 'r' in x1 or 's' in x1 or 't' in x1 or 'u' in x1 or 'v' in x1 or 'w' in x1 or 'x' in x1 or 'y' in x1 or 'z' in x1 or'A' in x1 or 'B' in x1 or 'C' in x1 or 'd' in x1 or 'E' in x1 or 'F' in x1 or 'G' in x1 or 'H' in x1 or 'I' in x1 or 'J' in x1 or 'K' in x1 or 'L' in x1  or 'M' in x1 or 'N' in x1 or 'O' in x1 or 'P' in x1 or 'Q' in x1 or 'R' in x1 or 'S' in x1 or 'T' in x1 or 'U' in x1 or 'V' in x1 or 'W' in x1 or 'X' in x1 or 'Y' in x1 or 'Z' in x1 or '/' in x1  or ';' in x1 or ':' in x1 or '!' in x1 or '@' in x1 or '#' in x1 or '$' in x1 or '%' in x1 or '^' in x1 or '&' in x1 or '*' in x1 or ')' in x1 or '(' in x1 or '<' in x1 or '>' in x1 or ',' in x1 or '`' in x1 or '~' in x1 or '+' in x1 or '=' in x1 or '_' in x1 or '?' in x1 or '[' in x1 or ']' in x1 or '{' in x1 or '}' in x1 or '|' in x1 or '"' in x1 or '\ ' in x1:

        print('enter a #NUMBER#')
        x1 = input('please enter a point value of x: ')
    else:
         if '.' not in x1:
             r = int(x1)
         else:
             r = float(x1)
while 'a' in x1 or 'b' in x1 or 'c' in x1 or 'd' in x1 or 'e' in x1 or 'f' in x1 or 'g' in x1 or 'h' in x1 or 'i' in x1 or 'j' in x1 or 'k' in x1 or 'l' in x1  or 'm' in x1 or 'n' in x1 or 'o' in x1 or 'p' in x1 or 'q' in x1 or 'r' in x1 or 's' in x1 or 't' in x1 or 'u' in x1 or 'v' in x1 or 'w' in x1 or 'x' in x1 or 'y' in x1 or 'z' in x1 or'A' in x1 or 'B' in x1 or 'C' in x1 or 'd' in x1 or 'E' in x1 or 'F' in x1 or 'G' in x1 or 'H' in x1 or 'I' in x1 or 'J' in x1 or 'K' in x1 or 'L' in x1  or 'M' in x1 or 'N' in x1 or 'O' in x1 or 'P' in x1 or 'Q' in x1 or 'R' in x1 or 'S' in x1 or 'T' in x1 or 'U' in x1 or 'V' in x1 or 'W' in x1 or 'X' in x1 or 'Y' in x1 or 'Z' in x1 or '/' in x1  or ';' in x1 or ':' in x1 or '!' in x1 or '@' in x1 or '#' in x1 or '$' in x1 or '%' in x1 or '^' in x1 or '&' in x1 or '*' in x1 or ')' in x1 or '(' in x1 or '<' in x1 or '>' in x1 or ',' in x1 or '`' in x1 or '~' in x1 or '+' in x1 or '=' in x1 or '_' in x1 or '?' in x1 or '[' in x1 or ']' in x1 or '{' in x1 or '}' in x1 or '|' in x1 or '"' in x1 or '\ ' in x1:
    print('enter a #NUMBER#')
    x1 = input('please enter a point value of x: ')
else:
    if '.' in x1:
        r = float(x1)
    else:
        r = int(x1)


print('')
y1=input('please enter a point value of y: ')
while y1=='':
    print('You have not entered a value')
    y1 = input('please enter a point value of y: ')


if '.' in y1:
        while 'a' in y1 or 'b' in y1 or 'c' in y1 or 'd' in y1 or 'e' in y1 or 'f' in y1 or 'g' in y1 or 'h' in y1 or 'i' in y1 or 'j' in y1 or 'k' in y1 or 'l' in y1 or 'm' in y1 or 'n' in y1 or 'o' in y1 or 'p' in y1 or 'q' in y1 or 'r' in y1 or 's' in y1 or 't' in y1 or 'u' in y1 or 'v' in y1 or 'w' in y1 or 'x' in y1 or 'y' in y1 or 'z' in y1 or 'A' in y1 or 'B' in y1 or 'C' in y1 or 'd' in y1 or 'E' in y1 or 'F' in y1 or 'G' in y1 or 'H' in y1 or 'I' in y1 or 'J' in y1 or 'K' in y1 or 'L' in y1  or 'M' in y1 or 'N' in y1 or 'O' in y1 or 'P' in y1 or 'Q' in y1 or 'R' in y1 or 'S' in y1 or 'T' in y1 or 'U' in y1 or 'V' in y1 or 'W' in y1 or 'X' in y1 or 'Y' in y1 or 'Z' in y1 or '/' in y1  or ';' in y1 or ':' in y1 or '!' in y1 or '@' in y1 or '#' in y1 or '$' in y1 or '%' in y1 or '^' in y1 or '&' in y1 or '*' in y1 or ')' in y1 or '(' in y1 or '<' in y1 or '>' in y1 or ',' in y1 or '`' in y1 or '~' in y1 or '+' in y1 or '=' in y1 or '_' in y1 or '?' in y1 or '[' in y1 or ']' in y1 or '{' in y1 or '}' in y1 or '|' in y1 or '"' in y1 or '\ ' in y1:

                print('enter a #NUMBER#')
                y1 = input('please enter a point value of y: ')
        else:
            if '.' in y1:
                r2=float(y1)
            else:
                r2=int(y1)
if '.' not in y1:
    while 'a' in y1 or 'b' in y1 or 'c' in y1 or 'd' in y1 or 'e' in y1 or 'f' in y1 or 'g' in y1 or 'h' in y1 or 'i' in y1 or 'j' in y1 or 'k' in y1 or 'l' in y1 or 'm' in y1 or 'n' in y1 or 'o' in y1 or 'p' in y1 or 'q' in y1 or 'r' in y1 or 's' in y1 or 't' in y1 or 'u' in y1 or 'v' in y1 or 'w' in y1 or 'x' in y1 or 'y' in y1 or 'z' in y1 or 'A' in y1 or 'B' in y1 or 'C' in y1 or 'd' in y1 or 'E' in y1 or 'F' in y1 or 'G' in y1 or 'H' in y1 or 'I' in y1 or 'J' in y1 or 'K' in y1 or 'L' in y1  or 'M' in y1 or 'N' in y1 or 'O' in y1 or 'P' in y1 or 'Q' in y1 or 'R' in y1 or 'S' in y1 or 'T' in y1 or 'U' in y1 or 'V' in y1 or 'W' in y1 or 'X' in y1 or 'Y' in y1 or 'Z' in y1 or '/' in y1  or ';' in y1 or ':' in y1 or '!' in y1 or '@' in y1 or '#' in y1 or '$' in y1 or '%' in y1 or '^' in y1 or '&' in y1 or '*' in y1 or ')' in y1 or '(' in y1 or '<' in y1 or '>' in y1 or ',' in y1 or '`' in y1 or '~' in y1 or '+' in y1 or '=' in y1 or '_' in y1 or '?' in y1 or '[' in y1 or ']' in y1 or '{' in y1 or '}' in y1 or '|' in y1 or '"' in y1 or '\ ' in y1:
        print('enter a #NUMBER#')
        y1 = input('please enter a point value of y: ')
    else:
         if '.' not in y1:
             r2 = int(y1)
         else:
             r2 = float(y1)
while 'a' in y1 or 'b' in y1 or 'c' in y1 or 'd' in y1 or 'e' in y1 or 'f' in y1 or 'g' in y1 or 'h' in y1 or 'i' in y1 or 'j' in y1 or 'k' in y1 or 'l' in y1 or 'm' in y1 or 'n' in y1 or 'o' in y1 or 'p' in y1 or 'q' in y1 or 'r' in y1 or 's' in y1 or 't' in y1 or 'u' in y1 or 'v' in y1 or 'w' in y1 or 'x' in y1 or 'y' in y1 or 'z' in y1 or 'A' in y1 or 'B' in y1 or 'C' in y1 or 'd' in y1 or 'E' in y1 or 'F' in y1 or 'G' in y1 or 'H' in y1 or 'I' in y1 or 'J' in y1 or 'K' in y1 or 'L' in y1  or 'M' in y1 or 'N' in y1 or 'O' in y1 or 'P' in y1 or 'Q' in y1 or 'R' in y1 or 'S' in y1 or 'T' in y1 or 'U' in y1 or 'V' in y1 or 'W' in y1 or 'X' in y1 or 'Y' in y1 or 'Z' in y1 or '/' in y1  or ';' in y1 or ':' in y1 or '!' in y1 or '@' in y1 or '#' in y1 or '$' in y1 or '%' in y1 or '^' in y1 or '&' in y1 or '*' in y1 or ')' in y1 or '(' in y1 or '<' in y1 or '>' in y1 or ',' in y1 or '`' in y1 or '~' in y1 or '+' in y1 or '=' in y1 or '_' in y1 or '?' in y1 or '[' in y1 or ']' in y1 or '{' in y1 or '}' in y1 or '|' in y1 or '"' in y1 or '\ ' in y1:
    print('enter a #NUMBER#')
    y1 = input('please enter a point value of y: ')
else:
    if '.' in y1:
        r2 = float(y1)
    else:
        r2 = int(y1)

print('')
x2=input('please enter a point value of x for the second point: ')

while x2=='':
    print('You have not entered a value')
    x2 = input('please enter a point value of x: ')
while str(x1)==str(x2):
    print('wrong value for x')
    y=os.system('pause')
    print('')
    x2 = input('please enter a point value of x: ')



if '.' in x2:
        while 'a' in x2 or 'b' in x2 or 'c' in x2 or 'd' in x2 or 'e' in x2 or 'f' in x2 or 'g' in x2 or 'h' in x2 or 'i' in x2 or 'j' in x2 or 'k' in x2 or 'l' in x2  or 'm' in x2 or 'n' in x2 or 'o' in x2 or 'p' in x2 or 'q' in x2 or 'r' in x2 or 's' in x2 or 't' in x2 or 'u' in x2 or 'v' in x2 or 'w' in x2 or 'x' in x2 or 'y' in x2 or 'z' in x2 or'A' in x2 or 'B' in x2 or 'C' in x2 or 'd' in x2 or 'E' in x2 or 'F' in x2 or 'G' in x2 or 'H' in x2 or 'I' in x2 or 'J' in x2 or 'K' in x2 or 'L' in x2  or 'M' in x2 or 'N' in x2 or 'O' in x2 or 'P' in x2 or 'Q' in x2 or 'R' in x2 or 'S' in x2 or 'T' in x2 or 'U' in x2 or 'V' in x2 or 'W' in x2 or 'X' in x2 or 'Y' in x2 or 'Z' in x2 or '/' in x2  or ';' in x2 or ':' in x2 or '!' in x2 or '@' in x2 or '#' in x2 or '$' in x2 or '%' in x2 or '^' in x2 or '&' in x2 or '*' in x2 or ')' in x2 or '(' in x2 or '<' in x2 or '>' in x2 or ',' in x2 or '`' in x2 or '~' in x2 or '+' in x2 or '=' in x2 or '_' in x2 or '?' in x2 or '[' in x2 or ']' in x2 or '{' in x2 or '}' in x2 or '|' in x2 or '"' in x2 or '\ ' in x2:
                print('enter a #NUMBER#')
                x2 = input('please enter a point value of x: ')
                while str(x1) == str(x2):
                    print('wrong value for x')
                    y = os.system('pause')
                    print('')
                    x2 = input('please enter a point value of x: ')
                    if '.' not in x2:
                        r3 = int(x2)
                    else:
                        r3 = float(x2)
        else:
            if '.' in x2:
                r3=float(x2)
            else:
                r3=int(x2)
if '.' not in x2:
    while 'a' in x2 or 'b' in x2 or 'c' in x2 or 'd' in x2 or 'e' in x2 or 'f' in x2 or 'g' in x2 or 'h' in x2 or 'i' in x2 or 'j' in x2 or 'k' in x2 or 'l' in x2  or 'm' in x2 or 'n' in x2 or 'o' in x2 or 'p' in x2 or 'q' in x2 or 'r' in x2 or 's' in x2 or 't' in x2 or 'u' in x2 or 'v' in x2 or 'w' in x2 or 'x' in x2 or 'y' in x2 or 'z' in x2 or'A' in x2 or 'B' in x2 or 'C' in x2 or 'd' in x2 or 'E' in x2 or 'F' in x2 or 'G' in x2 or 'H' in x2 or 'I' in x2 or 'J' in x2 or 'K' in x2 or 'L' in x2  or 'M' in x2 or 'N' in x2 or 'O' in x2 or 'P' in x2 or 'Q' in x2 or 'R' in x2 or 'S' in x2 or 'T' in x2 or 'U' in x2 or 'V' in x2 or 'W' in x2 or 'X' in x2 or 'Y' in x2 or 'Z' in x2 or '/' in x2  or ';' in x2 or ':' in x2 or '!' in x2 or '@' in x2 or '#' in x2 or '$' in x2 or '%' in x2 or '^' in x2 or '&' in x2 or '*' in x2 or ')' in x2 or '(' in x2 or '<' in x2 or '>' in x2 or ',' in x2 or '`' in x2 or '~' in x2 or '+' in x2 or '=' in x2 or '_' in x2 or '?' in x2 or '[' in x2 or ']' in x2 or '{' in x2 or '}' in x2 or '|' in x2 or '"' in x2 or '\ ' in x2:

        print('enter a #NUMBER#')
        x2 = input('please enter a point value of x: ')
        while str(x1) == str(x2):
            print('wrong value for x')
            y = os.system('pause')
            print('')
            x2 = input('please enter a point value of x: ')
            if '.' not in x2:
                r3 = int(x2)
            else:
                r3 = float(x2)
    else:
         if '.' not in x2:
             r3 = int(x2)
         else:
             r3 = float(x2)
while 'a' in x2 or 'b' in x2 or 'c' in x2 or 'd' in x2 or 'e' in x2 or 'f' in x2 or 'g' in x2 or 'h' in x2 or 'i' in x2 or 'j' in x2 or 'k' in x2 or 'l' in x2  or 'm' in x2 or 'n' in x2 or 'o' in x2 or 'p' in x2 or 'q' in x2 or 'r' in x2 or 's' in x2 or 't' in x2 or 'u' in x2 or 'v' in x2 or 'w' in x2 or 'x' in x2 or 'y' in x2 or 'z' in x2 or'A' in x2 or 'B' in x2 or 'C' in x2 or 'd' in x2 or 'E' in x2 or 'F' in x2 or 'G' in x2 or 'H' in x2 or 'I' in x2 or 'J' in x2 or 'K' in x2 or 'L' in x2  or 'M' in x2 or 'N' in x2 or 'O' in x2 or 'P' in x2 or 'Q' in x2 or 'R' in x2 or 'S' in x2 or 'T' in x2 or 'U' in x2 or 'V' in x2 or 'W' in x2 or 'X' in x2 or 'Y' in x2 or 'Z' in x2 or '/' in x2  or ';' in x2 or ':' in x2 or '!' in x2 or '@' in x2 or '#' in x2 or '$' in x2 or '%' in x2 or '^' in x2 or '&' in x2 or '*' in x2 or ')' in x2 or '(' in x2 or '<' in x2 or '>' in x2 or ',' in x2 or '`' in x2 or '~' in x2 or '+' in x2 or '=' in x2 or '_' in x2 or '?' in x2 or '[' in x2 or ']' in x2 or '{' in x2 or '}' in x2 or '|' in x2 or '"' in x2 or '\ ' in x2:
    print('enter a #NUMBER#')
    x2 = input('please enter a point value of x: ')
    while str(x1) == str(x2):
        print('wrong value for x')
        y = os.system('pause')
        print('')
        x2 = input('please enter a point value of x: ')
        if '.' not in x2:
            r3 = int(x2)
        else:
            r3 = float(x2)

else:
    if '.' in x2:
        r3 = float(x2)
    else:
        r3 = int(x2)

print('')
y2=input('please enter a point value of y for the second point: ')
#r=x1

while y2=='':
    print('You have not entered a value')
    y2 = input('please enter a point value of y: ')


if '.' in y2:
        while 'a' in y2 or 'b' in y2 or 'c' in y2 or 'd' in y2 or 'e' in y2 or 'f' in y2 or 'g' in y2 or 'h' in y2 or 'i' in y2 or 'j' in y2 or 'k' in y2 or 'l' in y2 or 'm' in y2 or 'n' in y2 or 'o' in y2 or 'p' in y2 or 'q' in y2 or 'r' in y2 or 's' in y2 or 't' in y2 or 'u' in y2 or 'v' in y2 or 'w' in y2 or 'x' in y2 or 'y' in y2 or 'z' in y2 or'A' in y2 or 'B' in y2 or 'C' in y2 or 'd' in y2 or 'E' in y2 or 'F' in y2 or 'G' in y2 or 'H' in y2 or 'I' in y2 or 'J' in y2 or 'K' in y2 or 'L' in y2  or 'M' in y2 or 'N' in y2 or 'O' in y2 or 'P' in y2 or 'Q' in y2 or 'R' in y2 or 'S' in y2 or 'T' in y2 or 'U' in y2 or 'V' in y2 or 'W' in y2 or 'X' in y2 or 'Y' in y2 or 'Z' in y2 or '/' in y2  or ';' in y2 or ':' in y2 or '!' in y2 or '@' in y2 or '#' in y2 or '$' in y2 or '%' in y2 or '^' in y2 or '&' in y2 or '*' in y2 or ')' in y2 or '(' in y2 or '<' in y2 or '>' in y2 or ',' in y2 or '`' in y2 or '~' in y2 or '+' in y2 or '=' in y2 or '_' in y2 or '?' in y2 or '[' in y2 or ']' in y2 or '{' in y2 or '}' in y2 or '|' in y2 or '"' in y2:


                print('enter a #NUMBER#')
                y2 = input('please enter a point value of y: ')
        else:
            if '.' in y2:
                r4=float(y2)
            else:
                r4=int(y2)
if '.' not in y2:
    while 'a' in y2 or 'b' in y2 or 'c' in y2 or 'd' in y2 or 'e' in y2 or 'f' in y2 or 'g' in y2 or 'h' in y2 or 'i' in y2 or 'j' in y2 or 'k' in y2 or 'l' in y2 or 'm' in y2 or 'n' in y2 or 'o' in y2 or 'p' in y2 or 'q' in y2 or 'r' in y2 or 's' in y2 or 't' in y2 or 'u' in y2 or 'v' in y2 or 'w' in y2 or 'x' in y2 or 'y' in y2 or 'z' in y2 or'A' in y2 or 'B' in y2 or 'C' in y2 or 'd' in y2 or 'E' in y2 or 'F' in y2 or 'G' in y2 or 'H' in y2 or 'I' in y2 or 'J' in y2 or 'K' in y2 or 'L' in y2  or 'M' in y2 or 'N' in y2 or 'O' in y2 or 'P' in y2 or 'Q' in y2 or 'R' in y2 or 'S' in y2 or 'T' in y2 or 'U' in y2 or 'V' in y2 or 'W' in y2 or 'X' in y2 or 'Y' in y2 or 'Z' in y2 or '/' in y2  or ';' in y2 or ':' in y2 or '!' in y2 or '@' in y2 or '#' in y2 or '$' in y2 or '%' in y2 or '^' in y2 or '&' in y2 or '*' in y2 or ')' in y2 or '(' in y2 or '<' in y2 or '>' in y2 or ',' in y2 or '`' in y2 or '~' in y2 or '+' in y2 or '=' in y2 or '_' in y2 or '?' in y2 or '[' in y2 or ']' in y2 or '{' in y2 or '}' in y2 or '|' in y2 or '"' in y2:

        print('enter a #NUMBER#')
        y2 = input('please enter a point value of y: ')
    else:
         if '.' not in y2:
             r4 = int(y2)
         else:
             r4 = float(y2)
while 'a' in y2 or 'b' in y2 or 'c' in y2 or 'd' in y2 or 'e' in y2 or 'f' in y2 or 'g' in y2 or 'h' in y2 or 'i' in y2 or 'j' in y2 or 'k' in y2 or 'l' in y2 or 'm' in y2 or 'n' in y2 or 'o' in y2 or 'p' in y2 or 'q' in y2 or 'r' in y2 or 's' in y2 or 't' in y2 or 'u' in y2 or 'v' in y2 or 'w' in y2 or 'x' in y2 or 'y' in y2 or 'z' in y2 or'A' in y2 or 'B' in y2 or 'C' in y2 or 'd' in y2 or 'E' in y2 or 'F' in y2 or 'G' in y2 or 'H' in y2 or 'I' in y2 or 'J' in y2 or 'K' in y2 or 'L' in y2  or 'M' in y2 or 'N' in y2 or 'O' in y2 or 'P' in y2 or 'Q' in y2 or 'R' in y2 or 'S' in y2 or 'T' in y2 or 'U' in y2 or 'V' in y2 or 'W' in y2 or 'X' in y2 or 'Y' in y2 or 'Z' in y2 or '/' in y2  or ';' in y2 or ':' in y2 or '!' in y2 or '@' in y2 or '#' in y2 or '$' in y2 or '%' in y2 or '^' in y2 or '&' in y2 or '*' in y2 or ')' in y2 or '(' in y2 or '<' in y2 or '>' in y2 or ',' in y2 or '`' in y2 or '~' in y2 or '+' in y2 or '=' in y2 or '_' in y2 or '?' in y2 or '[' in y2 or ']' in y2 or '{' in y2 or '}' in y2 or '|' in y2 or '"' in y2:
    print('enter a #NUMBER#')
    y2 = input('please enter a point value of y: ')
else:
    if '.' in y2:
        r4 = float(y2)
    else:
        r4 = int(y2)

if len(x1)>=2:
    if x1[1]!='.' and x1[0]!='-':
        r=int(x1)
if len(y1)>=2:
    if y1[1]!='.' and y1[0]!='-':
        r2=int(y1)
if len(x2)>=2:
    if x2[1]!='.' and x2[0]!='-':
        r3=int(x2)
if len(y2)>=2:
    if y2[1]!='.' and y2[0]!='-':
        r4=int(y2)

#print(r,type(r))
#print(r2,type(r2))
#print(r3,type(r3))
#print(r4,type(r4))

z=(r2-r4)/(r-r3)
x1,x2,y1,y2=str(x1),str(x2),str(y1),str(y2)

p1,p2='('+str(r)+','+y1+')','('+x2+','+y2+')'

print('point 1:',p1)
print('point 2:',p2)
if z<0:
    if str(z)[-1]!='0':
        print('The slope:',z)
    else:
        print('The slope:',str(z)[:-2])
elif str(z)[:-2]=='-0':
    print('The slope: 0')
else:
    if str(z)[-1]!='0':
        print('The slope:',z)
    else:
        print('The slope:',str(z)[:-2])
