#Merge two lists
import random


def insertionSort(alist):
  for index in range(1,len(alist)):
    currentVal = alist[index]
    pos= index
    while pos >0 and alist[pos-1]>currentVal:
      alist[pos]=alist[pos-1]
      pos= pos-1
    alist[pos] = currentVal
    
      
      
#x= int(input())           #input deciding the lenght of list 
#a =[19,21,36]					
#b= [18,27,32]

# for i in range(x):
#   #a.append(int(input()))
#   #b.append(int(input()))
#   a.append(random.randint(0,11))
#   b.append(random.randint(-6,15))

a=random.sample(range(1,50),3)
b=random.sample(range(1,50),3)

#print(a)
insertionSort(a)
#print(a)
print(list(a))
insertionSort(b)

#print(b)
print(list(b))

#t=True
for j in range(len(a)):
  t,y=True,True
  #print(j,'j')
  for i in range(0,len(b)):
    #print(i,'i')
    if b[j] >a[i] and b[j]<a[i+1]:
      a.insert(i+1,b[j])
    elif b[j]<a[i] and t==True:
      a.insert(i,b[j])
      t=False
    elif b[j]>max(a) and y==True:
      a.append(b[j])
      y=False
      break
    elif b[j]>a[i] and i>1:
      a.insert(i+1,b[j])
    else:
      continue
    
print(a)


