#Check if an array can be divided into pairs whose sum is divisible by k

print('enter the range of list')
y= int(input())
x=[]
for i in range(y):
  x.append(int(input()))
print('enter the Number divisible by')
l=int(input())

#print(x)
#print(len(x))
p=[]
for i in range(len(x)):
  for j in range(i+1,len(x)):
    #print(x[i]+x[j])
    if (x[i]+x[j])%l==0:
      #print(x[i],i)
      #print(x[j],j)
      p.append((x[i],x[j]))
      
      
print(p)



#input
# 2 , 4 ,8
# k =2
#output - 
#[(2, 4), (2, 8), (4, 8)]