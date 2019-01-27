s=""
o=""
z=input('write sentese for encrypt ')+'   '
y=0
#y=int(input('Select a number to move the letters and encrypt it '))
for y in range(24):
    for x in z:
	     if ord(x)>=ord('a') and ord(x)<=ord('z'):
		     o+=chr((ord(x)+y-ord('a'))%26+ord('a'))
	     else:
	         o+=x
print(o)
print('') 