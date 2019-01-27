num=int(raw_input("write number between 50 to 100 "))
if 50>num :                  #The program shows all the numbers that divide by three with no remainder
    print ('you cant enter that number')
elif num>100 :
        print ('you cant enter that number')
else :
   i=-1
   for i in xrange(50,num+1)  :
    if  i%3==0:
        print i