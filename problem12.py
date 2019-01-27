import func
s,a=0,0
z=func.trinum()
print(z[10000])
for t in z[10000:]:
    s=0
    for f in range(1,t//2+1):
        print(t)
        if t%f==0:
            print(f)
            s+=1
            if s==500:
                print(t,s,f)
                exit(0)
        else:
            pass