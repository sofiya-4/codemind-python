n=int(input())
lst=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(0,n):
    if(i%2==0):
        sum1+=lst[i]
    else:
        sum2+=lst[i]
if(sum1>sum2):
    print(sum1-sum2)
else:
    print(sum2-sum1)