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
    #print(l)
    str1="".join(l[0:i])
    #print(str1)
  else:
    pos= i
    #print(i)
    b[0]=k[i]
    k[i] = str(random.randint(0,9))
    ##
    #Code needs to be added to make it full proof i.e. to pass all test cases.
    ##
    while k[i]==b[0]:
      k[i]=str(random.randint(0,9))
    l.insert(i,k[i])
    str1= "".join(l[0:i])+str(l[i])+"".join(l[i+1:])

# #l=list(l)
# str1="".join((l[0:4]))
# str1=str1+str(l[4])
# #n="".join(l)
print(str1)    
#
# Motive of the code is to replace the repeated elements with a new random number . Can be replaced with a particular number also.
#  