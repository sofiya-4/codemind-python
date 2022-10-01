n=int(input())
s1=0
s2=1
while(n!=0):
    r=n%10 #4
    s1=s1+r  #s1=4
    s2=s2*r  #s2 =4
    n=n//10  #n=23
print(abs(s1-s2))