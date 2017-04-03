import random
import numpy as np
def matrix(row,column):
  
  x=[]
  #y=[]											was creating an empty list to append in line 11 - ** 
  #row=int(input())
  #column=int(input())
    
  for i in range(row):
    x.append([])						# ** - was appending empty list which was created earlier and alloted a memory, because of which all rows were having all values - Explained better after program
    
  #print(x)
    
  for i in range(row):
    for j in range(column):
      x[i].insert(j,random.randint(1,5))			#input the numbers randomly
      #x[i].append(int(input()))
    
  #print([id(i) for i in x])						#Very important to find out if the list is getting repeated in every ROW
  
  return x
  

q=matrix(int(input()),int(input()))
print(q)

e=matrix(int(input()),int(input()))
print(e)

mx = np.matrix(q)						#numpy used which helps in matrix multiplication
my=np.matrix(e)

print(mx*my)


#if you try to append a list which was created earlier, then the input would look like
#for 2*2 matrix
#input - 1,2,3,4
#output- [[1,2,3,4][1,2,3,4]
#This was occuring because changes were being done at the same location, came to know by printing the ID of the element in the list.

