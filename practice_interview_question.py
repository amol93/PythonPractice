#Input- 123456

#Output: [ 33456, 15456, 12756, 12396 , 123411 ]

x= input()
#print(x)

x=list(x)
o=x
#print(x)
z=[]
e=[]
for i in range(len(x)):
  if i+1 ==len(x):
    break
  else:
    y=int(x[i])+int(x[i+1])
    y=str(y)
    z.append(y)
    #print(z)
#print(z,'z')
#print(x)
q=[]
for i in range(len(x)):
  if i==0:
    e.append(z[i])
    for element in x:
      if element!=x[i] and element!=x[i+1]:
        e.append(str(element))
    l=''.join(e)
    q.append(l)
    e=[]
  if i>0 and i<len(x)-1:
    
    # for element in x:
    # if element!=x[i] and element!=x[i+1]:
    #     e.append(str(element))
    
    for el in range(i):
      e.insert(i,x[el])
    e.append(z[i])
    #print(e)
    for i in range(i+2,len(x)):
      e.append(x[i])
      #print(e)
    l=''.join(e)
    q.append(l)
    
    e=[]
    
print(q)  
#print(e)

#print(int(x[0])+int(x[1]))
