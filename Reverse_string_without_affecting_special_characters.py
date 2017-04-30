#Reverse a string without affecting special characters  
#Input string: a!!!b.c.d,e'f,ghi
#Output string: i!!!h.g.f,e'd,cba

#Input Example string: @#!$
#Output Example String: @#!$

x=input()
r=0
y=[]
for i in range(len(x)-1,-1,-1):
  if x[i] == '@' or x[i]=='#' or x[i]=='$' or x[i]=='!' or x[i]=='.' or x[i]=="'" or x[i]==',':
      continue
  y.append(x[i])
  a=''.join(y)
  
#print(a)        #For testing
for i in range(0,len(x)):
  if x[i] == '@' or x[i]=='#' or x[i]=='$'or x[i]=='!' or x[i]=='.'or x[i]=="'" or x[i]==',':
    y.insert(i,x[i])
    a=''.join(y)
    #print(a)
  
for i in range(0,len(x)):
  if x.find('$')!=-1 or x.find('#')!=-1 or x.find('!')!=-1 or x.find('.')!=-1 or x.find("'")!=-1 or x.find('.')!=-1:
    r+=1
    
  if r==len(x):
    a=x

  
  
print(a) # Final Output