n=int(input())
lst=list(map(int,input().split()))
sum1=0
for i in range(0,n):
    if(lst[i]%2==0):
        sum1+=lst[i]
print(sum1)