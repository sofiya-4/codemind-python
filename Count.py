m=int(input())
n=map(int,input().split())
c=0
e=0
for i in n:
    if i%2==0:
        c+=1
    else:
        e+=1
print(c,e,end=" ")