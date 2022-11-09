n=input()
x=input()
for i in n:
    if x==i:
        print(True)
        print(n.index(i))
        break
else:
    print(False)