def sort(alist):
      for i in range(len(alist)-1,0,-1):
          for j in range(i):
              if alist[j]>alist[j+1]:
                  temp = alist[j]
                  alist[j]=alist[j+1]
                  alist[j+1]=temp
  
      return alist

def median(a):
  if len(a)%2==0:
          #print('if statment')
    u = len(z)//2
    u1 = u-1
    v=u1+1
    median = (a[u1]+a[v])/2
  else:
    u = len(a)//2
    median = a[u]
        
  return median
q=[]
e=[]
x , y= int(input()),int(input()) 
for i in range(x):
  q.append(int(input()))
for i in range(y):
  e.append(int(input()))
z=[]
z.extend(q)
z.extend(e)
        #print(z)
print(sort(z))
print(median(z))