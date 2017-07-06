 import random
 a = input("Enter a 5 dit num")
 #print(a)
 #print(len(a))
 k=[] # list to separate the integers
 for i in range(0,len(a)):
   k.append(a[i])
  
 print(k)
 l=[] #list for comparison
 b=[0,0,0,0,0] # list created to check random number which is replacing the current number is not the same 
 for i in range(0,len(a)):
   if k[i] not in l:
     l.append(k[i])
#     #print(l)
   else:
     pos= i
     print(i)
     b[0]=k[i]
     k[i] = int(random.randint(0,9))
     while k[i]==b[0]:
       k[i]=random.randint(0,9)
     l.insert(i,k[i])

 l=list(l)
 l=''.join((l))
 l="".join(l)
 print(l)      
 
 