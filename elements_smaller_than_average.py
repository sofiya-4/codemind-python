n=int(input())
lst=list(map(int,input().split()))
c=0
a=(sum(lst))//n
for i in range(n):
    if(lst[i]<=a):
        c+=1
print(c)