elements = input().strip().split(' ')
a = int(elements[0]) # inpput number
t = int(elements[1]) #Number of swaps to be performed on the input number


a=list(str(a))
#print a

#a.sort()
#print a
swap =0
#a.reverse()

for num in range(len(a)-1,0,-1):
  #print num
  #swap =swap +1
  for i in range(num):
    #print i
    if a[i]<a[i+1] :
      swap =swap +1
      temp = a[i]
      a[i]=a[i+1]
      a[i+1]=temp
      #print a
      #print swap
    if swap ==t:
      break
  
print (a)  
  

result="".join(a)

print (result)



##Input =1234 2
##Output = 3214