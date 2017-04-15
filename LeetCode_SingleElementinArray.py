#Input: [1,1,2,3,3,4,4,8,8]
#Output: 2

#Input: [3,3,7,7,10,11,11]
#Output: 10


def Nonduplicate(alist):
  y={}								#creating a dictionary
  for i in alist:
    if i not in y:
      y[i] = 0						#initialising 
      #y.values = 1
    if i in y:
      y[i] +=1
  
  z= min(y,key=y.get)				#finding the minimmum key in the list 
  return z


x=[]									#creating a list
o= int(input())
for i in range(o):
  x.append(int(input()))
  
print(Nonduplicate(x))
