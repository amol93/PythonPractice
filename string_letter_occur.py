def outString(n):
#n=input()
  a= list()
  for i in range(len(n)):
    a.append(str(n[i]))
  #print(a)
  a.sort()
  #print(a)
  
  
  d={}
  for i in range(len(n)):
    if a[i] not in d:
      d[a[i]] = 1
    else:
      d[a[i]]+=1
  v=[]
  for key,value in sorted(d.items()):
    v.append(value)
  #print(v)
  l=[]
  for i in range(len(n)):
    if a[i] not in l:
      l.append(a[i])
  #print(l)
  p=[]
  for i in range(len(l)):
    p.append(l[i])
    p.append(str(v[i]))
    
  p=''.join(p)
  return p
#print(p)

x=input()
e=outString(x)
print(e)

# i/p- heeleo
# o/p - e3h1l1o1

# i/p- engineer
# o/p- e3g1i1n2r1




