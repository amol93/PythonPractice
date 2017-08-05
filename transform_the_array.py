#Eg1
#Input [2, 4, 0, 4, 6, 7, 8, 0, 8, 1, 0, 2]
#Output 2 8 6 7 16 1 2 0 0 0 0 0

#Eg2
#Input 2 4 5 0 0 5 4 8 6 0 6 8
#Output 2 4 10 4 8 12 8 0 0 0 0 0 


#Eg3 
# input 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 3, 1
# output 2 2 6 1 0 0 0 0 0 0 0 0 0 0 0 

x= int(input("number of test cases"))
y= int(input("An integer"))
a=[]
for i in range(y):
  a.append(int(input()))
print(a)

for i in range(len(a)):
  if a[i]!=0:
    continue
  else:
    #print(i)
    a.remove(a[i])
    a.append(0)
    
    
print("appending 0 at the end- ",a)
for i in range(len(a)):
  if i+1<len(a):
    if a[i]==a[i+1]:
      a[i]*=2
      #print('ji')
      a[i+1]=0
#print("after doing the required manipulation- ",a)

for i in range(len(a)):
  if i+1 < len(a):
    if a[i]==0:
      a.append(0)
      a.pop(i)

print(a)