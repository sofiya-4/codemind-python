x=int(input())
i=1
s=0
while(i<=x):
    if(x%i==0):
        s+=1
    i+=1
if(s==2):
    print("prime")
else:
    print("not a prime")
        