s1=input()
s1=s1.lower()
s1=list(s1.split())
s2=input()
s2=s2.lower()
s2=list(s2.split())
c=0
for i in range(len(s1)):
    if s1[i] in s2 and s2.count(s1[i])==1 and s1[i]!=" " and s1.count(s1[i])==1:
        c+=1
print(c)
