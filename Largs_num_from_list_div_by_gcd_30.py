
### function to make permutations of a string 
def rec(a):
  if len(a)==0:
    return
  elif len(a)==1:
    return a
  else:
    p=[]
    for i in range(len(a)):
      x=a[i]
      xs = a[:i]+a[i+1:]
      for j in rec(xs):
        p.append(x+j)
        
  return p  

n=[]

## input
x=int(input())
for i in range(x):
  n.append(input())
m=n # transferring data to store original data for further use if needed.
#print(m)
e=[]
n=''.join(n)
print(n)


#Deleting a element to find permutations of string
for i in range((x)):
  m=m[:i]+m[i+1:]
  print(m,'i')
  e.append(''.join(m))
  if len(m)<len(n):
    m=n
print(m)    
#print(e,'e')
#print(n)
#str(n)  
e.append(n)
#print(e,'e')
l=[]
for i in range(len(e)):
  l.append(rec(e[i]))
print(l)


    
for i in range(len(l)):
  if int(l[i])%2==0 and int(l[i])%3==0 and int(l[i])%5==0 :
    print(l[i])
  else:
    continue

        
    