T=int(input())
for j in range(T):
    n=int(input())
    n1=n
    while True:
        fc=0
        
        for i in range(1,n1+1):
            if n1%i==0:
                fc+=1
        if fc==2:
            break
        n1+=1
    n2=n
    while True:
        pc=0
        
        for i in range(1,n1+1):
            if n2%i==0:
                pc+=1
        if pc==2:
            break
        n2-=1
    if n-n2<=n1-n:
        print(n2)
    else:
        print(n1)
