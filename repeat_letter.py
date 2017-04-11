x= input()					#taking input
#print(x)
#print(len(x))
boole= True					
for i in range(0,len(x)):
  for j in range(i+1,len(x)):
    if x[i]==x[j] and boole:		#Comparing elements of input
      #print(x[j])
      r=j 
      boole=False					#if elements match, boole=> Fals, so that again it does not enter loop
    #j=j+1
  
#print(x[r])
print(x[:r])						#printing elements which occur once
print(x[r:])						#printing element from the repeaated letter in th input







#Input = abcdefghijklmnopfghijkl
#output- abcdefghijklmnop
#	   - fghijkl