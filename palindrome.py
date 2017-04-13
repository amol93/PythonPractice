#palindrome

x= input()

y=[]

for i in range(len(x)-1,-1,-1):
  y.append(x[i])
  z=''.join(y)
  
if x==z:
  print('input is a palindrome')
else:
  print('it is not a palindrome')


