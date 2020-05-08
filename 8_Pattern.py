s='abcdefgfedcba'
print(s)
s=s.replace('g','_')
print(s)

for i in range(5,0,-1):
    s=s.replace(s[i],'_')
    print(s)
    
    
  
