n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
for i in range(len(l)):
    if(l1[i]%2)==0:
        print(l1[i])
        break
    else:
        continue