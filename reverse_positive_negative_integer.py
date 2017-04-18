#Reverse an integer

x= (input())
#print(x)
y=[]
x=list(x)
#print(x)
if x[0] == '-':
  for i in range(len(x)-1,-1,-1):
    y.append(x[i])
  y.insert(0,'-')
  y.pop()
else:
  for i in range(len(x)-1,-1,-1):
    y.append(x[i])

#print(y)
y=''.join(y)
print(y)


#Input -6903
#output -3096