#Find common elements in three sorted arrays/ lists

def sortThreeLists (a,v,c):
  d=[]
  for i in range(max(len(a),len(v),len(c))):
    if max(len(a),len(v),len(c)) == len(a):
      if a[i] in v and c:
        d.append(a[i])
    elif max(len(a),len(v),len(c)) == len(c):
      if c[i] in a and v:
        d.append(c[i])
    elif max(len(a),len(v),len(c)) == len(v):
      if v[i] in a and c:
        d.append(v[i])
	else:
		continue

  return d


r=[]
for i in range(int(input("Input the number for elements in the list \n"))):
  r.append(int(input()))
  
s=[]
for i in range(int(input("Input the number for elements in the list \n"))):
  s.append(int(input()))
  
t=[]
for i in range(int(input("Input the number for elements in the list \n"))):
  t.append(int(input()))

l=[]
l=sortThreeLists(r,s,t)
print(l)


#Input the number for elements in the first list 
#3
# 6
# 9
# 12
#Input the number for elements in the second list 
#4
#6
#12
#8
#20
#Input the number for elements in the third list 
#2
#6
#12
#[6, 9, 12] [6, 12, 8, 20] [6, 12]
#[6, 12] OUTPUT
