
s=input()
for i in s:
    a.append(i)

step=0
for i in range(len(a)-1):
    if(a[i]=='-' and a[i+1]=='+'):
        a[i]='+'
        a[i+1]='+'
        step=step+1
    elif(a[i]=='+' and a[i+1]=='-'):
        a[i]='+'
        a[i+1]='-'
        step=step+1
print(step)
