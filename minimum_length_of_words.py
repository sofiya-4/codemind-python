s=input()
s=s.split()
l1=[]
for i in s:
    l1.append(len(i))
print(min(l1))