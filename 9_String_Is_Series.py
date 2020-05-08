s="bacbcc"
l=[]
a=[]
for i in s:
    if(i not in l):
        l.append(i)
        a.append(s.count(i))
    
#print(a)
for i in range(1,max(a)+1):
    if(i not in a):
        print("No")
    else:
        print("Yes")
        break
    
