n=int(input())
lst=list(map(int,input().split()))
l1=lst[::-1]
s=0
lst=0
for i in l1:
    s=s+(i*pow(2,lst))
    lst+=1
    
print(s)