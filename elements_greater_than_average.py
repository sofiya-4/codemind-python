n=int(input())
lst=list(map(int,input().split()))
a=(sum(lst))//n
s=0
for i in range(n):
    if(lst[i]>=a):
        s+=1
print(s)