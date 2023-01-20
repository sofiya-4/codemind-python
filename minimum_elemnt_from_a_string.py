s=input()
s=list(s)
s.sort()
n="abcdefghijklmopqrstuvwxyz"
n1="ABCDEFGHIJKLMOPQRSTUVWXYZ"
for  i in range(len(n)):
    if n[i] in s:
        print(n[i])
        break
    elif n1[i] in s:
        print(n1[i])
        break