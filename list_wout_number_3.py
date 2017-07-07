def funOne(n):
  a=[]
  i=1
  while(i<n):
    if (i//10 ==3) or (i%10 ==3):
      a.append(i)
      #print(a)
      
    elif (i>99 and i<1000):
      j=i//10
      if(j//10 ==3) or (j%10 ==3):
        a.append(i)
    
    i=i+1
  return a 
        
m= int(input())
x = funOne(m)
#print(x)
print(len(x))
y = m-len(x)
print(y) #prints total numbers without number 3 in them