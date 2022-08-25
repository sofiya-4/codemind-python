N=int(input())
max=0
while(N>0):
    a=N%10
    if(max<a):
        max=a
    N=N//10
print(max)
        
    