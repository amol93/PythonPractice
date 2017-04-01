x =input()
x=list(x)
#print(x)
y=list(x)

# y="".join(x[:2])
# #print(y)
# z= "".join(x[2:])
# #print(z)
# #print(y+z)
l=[]
a=[]
#count =0
for i in range(0,len(x)):
    if i==0:
      (y[i])=int(x[i])+int(x[i+1])
      #print(x[i])
      d=str(y[i])
      a.append(d)
      print(a)
      for b in x:
        if b != x[i] and b!=x[i+1]:
          print(b)
          a.append(str(b))
      #print(a)
      h="".join(a)
      
      print(h)
      l.append(h)
      a=[]
      #print(l)
      #print(x)
    if i<len(x)-1 and i>0:
      y[i]=int(x[i])+int(x[i+1])
      #print(x[i])
      count =True
      d=str(y[i])
      for b in x:
        if b != x[i] and b!=x[i+1]:
          print(b)
          a.append(str(b))
          
      a.insert(i,d)
      p="".join(a)
      #print(h)
      l.append(p)
      a=[]
        
          
      #h="".join(a)
# e=",".join(h)
# print(e)
print(l)