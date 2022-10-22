n=int(input())
x=list(map(int,input().split()))
l1=[]
for i in x:
    x=str(i)
    y=len(x)
    l1.append(y)
e=l1.count(min(l1))
print(e)