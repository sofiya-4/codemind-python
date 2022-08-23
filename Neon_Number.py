a=int(input())
b=a*a
sum1=0
while b>0:
    sum1=sum1+b%10
    b=b//10
if(sum1==a):
    print("Neon Number")
else:
    print("Not Neon Number")
    
