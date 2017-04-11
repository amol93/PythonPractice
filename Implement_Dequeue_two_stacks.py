#implement dequeue using two stacks
from pythonds.basic.stack import Stack # learn more: https://python.org/pypi/pythonds

x,y,z=[],[],[]
s1= Stack()
s2= Stack()
s3= Stack()

for i in range(10):
  s1.push(i)
  #print(i)
  while i<9 and s1.isEmpty() == False:
    s2.push(s1.pop())
    #print(i)
    while s2.isEmpty() == False:
      s3.push(s2.pop())
    #print(s3.peek() ,'s3')
    s2.push(s3.pop())
    #print(s2.peek(),'s2')
  
print(s1.peek())
print(s3.isEmpty())
print(s3.peek())
print(s2.peek())

for i in range(10):				#printing s2
  if s2.isEmpty() == False:
    x.append(s2.pop())

print(x)

for i in range(10):			#printing s1
  if s1.isEmpty() == False:
    y.append(s1.pop())

print(y)

for i in range(10):				#printing s3
  if s3.isEmpty() == False:
    z.append(s3.pop())

print(z)


