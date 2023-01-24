s=input()
s=s.lower()
s=list(s.split())
y=input()
y=y.lower()
y=list(y.split())
for i in range(len(y)):
    if y[i] in s:
        print(y[i],end=" ")
