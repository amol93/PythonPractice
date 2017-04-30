#Find the biggest substring which is a palindrome


x=input()

maxlen=1

start = 0
low,high =0,0

for i in range(1,len(x)):
  low=i-1
  high=i
  
  while low>=0 and high<len(x) and x[low]==x[high]:
    #print(low,high)
    if high-low+1>maxlen:
      #print('loop1')
      start = low
      maxlen=high-low+1 
    low-=1 
    high+=1 
  #print('hello')
  
  low= i-1
  high = i+1 
  while low>=0 and high<len(x) and x[low]==x[high]:
    #print('loop2')
    if high-low+1>maxlen:
      #print('00000')
      start = low
      maxlen=high-low+1 
    low-=1 
    high+=1 
    
print("Longest palindrome substring is = " + x[start:start + maxlen])