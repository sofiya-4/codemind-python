n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(0,len(l),1):
    if(l[i]%2==0):
        l1.append(l[i])
    if(l[i]%2!=0):
        l2.append(l[i])
l3=l1+l2
print(*l3)