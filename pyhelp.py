import sys as s
import func
x,y=str(s.argv[1]),0

if x=='-h':
    x=input('usage: [encrypt / multicalc / crusher / fib / powme / palindrome] -r            ')
    if x=='encrypt -r':
        func.encrypter()
    if x=='powme -r':
        y=int(input('choose a number to power by himself:  '))
        func.powme(y)
    if x=='multicalc -r':
        func.multicalc()