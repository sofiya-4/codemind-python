n=int(input())
lst=list(map(int,input().split()))
l1=[]
for i in range(n):
    if(lst[i]%2==0):
        l1.append(i)
print(l1[-1])
