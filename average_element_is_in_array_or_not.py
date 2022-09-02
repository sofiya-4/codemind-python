N=int(input())
l=list(map(int,input().split()))
x=sum(l)
y=x//N
if y in l:
    print("True")
else:
    print("False")
