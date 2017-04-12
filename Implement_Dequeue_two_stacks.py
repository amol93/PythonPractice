#implement dequeue using two stacks
from pythonds.basic.stack import Stack # learn more: https://python.org/pypi/pythonds
#import random 

x,y,z=[],[],[]
s1= Stack()
s2= Stack()
s3= Stack()									#It is used for intermediate / temporary stack 
n=int(input())
for i in range(n):
  s1.push(i)
  print(i,'pushed in s1')
  while i<n-1 and s1.isEmpty() == False:
    while s2.isEmpty()==False:
      s3.push(s2.pop())
      print(s3.peek(),'Pushed into s3')
    s2.push(s1.pop())
    print(s2.peek(),'pushed in s2')
    while s2.isEmpty() == False:
      s3.push(s2.pop())
      print(s3.peek() ,'pushed in s3')
    while s3.isEmpty()==False:
      s2.push(s3.pop())
      print(s2.peek(),'pushed from s3 to s2')
      

  
# print(s1.peek())
# print(s3.isEmpty())
#print(s2.peek(),'top element in s2')
# print(s2.peek())

for i in range(10):			#printing s1
  if s1.isEmpty() == False:
    y.append(s1.pop())

print(y, 'numbers in s1')

for i in range(10):				#printing s2
  if s2.isEmpty() == False:
    x.append(s2.pop())

print(x,'numbers in s2')

for i in range(10):				#printing s3
  if s3.isEmpty() == False:
    z.append(s3.pop())

print(z,'numbers in s3') # since used as a temporary stack, it remains empty

#Output
# in s1 =[9]
# in s2 = [0,1,2,3,4,5,6,7,8]
# in s3 =[]
#

