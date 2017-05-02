import math

def pythTriplet(alist):
  for j in range(len(alist)-1):
    k = math.pow(x[j],2) + math.pow(x[j+1],2)
    #print(int(k))
    
    if math.sqrt(k) in x:
      return (x[j],x[j+1] ,int(math.sqrt(k)))
    else:
      continue
  
n=int(input())
x=[]
for i in range(n):
  x.append(int(input()))
#print(x)

print("Pythgorean triplet = ",pythTriplet(x))