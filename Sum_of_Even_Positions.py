n=int(input())
lst=list(map(int,input().split()))
sum=0
for i in range(0,n):
    if(i%2==0):
        sum+=lst[i]
print(sum)