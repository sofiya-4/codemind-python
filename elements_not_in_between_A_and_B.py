n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in l:
    if i<a or i>b:
        s=s+i
        print(i,end=" ")
else:
    if(s==0):
            
        print(-1)
        
        
