import time
x1=(time.time())#Start Time 
x=[1,2,2,4,5]			#Given range input
y,z=[],[]
for i in range(len(x)):
  if x[i] not in y:
    y.append(x[i])
for i in range(1,len(x)+1):
  if i not in z:
    z.append(i)

a=[set(z)-set(y)]  
#print(z.differnce(y))
  
#print(z)
#print(y)
print(a)
x2=(time.time())		#End Time
print(float(x2-x1))

#Expcted output- 3 
#Complexity - o(n) 