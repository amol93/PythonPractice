#Input a list and target number
#Aim is to find the target in the list such that addition of two consecutive elements of list is equal to target number
#eg lst =[2 ,1, 4 , 5] and target = 9
# Output = [2,3] indicating the target can be achieved by adding index 2 and 3
#if target num is found, it breaks the loop and code ends


target= int(input())
nums = list(map(int,input().split()))
t=[]
#print(len(nums))
#print(nums)
for i in range(len(nums)+1):
  #print(i)
  if i in (range(len(nums)-1)):
    t.append(nums[i]+nums[i+1])
  #print(t)
  if target in t:
    print([i,i+1])
    break
  elif i == len(nums):
    print("target cannot be found with the given set of input list")
  else:
    continue