n=input()
n=n.lower()
n=list(n.split())
m=input()
m=m.lower()
m=list(m.split())
c=0
for i in range(len(n)):
    if n[i] in m:
        c+=1
print(c)