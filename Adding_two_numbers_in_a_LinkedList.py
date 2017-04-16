# class Node:
  
#   def __init__ (self,init_data):
#     self.data = init_data
#     self.next = None
    
#   def getData(self):
#     return self.data
    
#   def setData(self,newData):
#     self.data = newData
    
#   def setNext(self,newNext):
#     self.next = newNext
    
#   def getNext(self):
#     return self.next

class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
  
  def __init__(self):
    self.head = None
  
  def addData(self,Data):
    temp = Node(Data)
    temp.next=self.head
    self.head = temp
    
  def printl(self):
    node=self.head
    while node!=None:
      print(node.data)
      node=node.next
      
  def addtwoList(self,alist1,alist2):
    prev= None
    carry =0
    temp = None
    
    while (alist1 is not None or alist2 is not None):
      #print(alist1.data,"alist1.getData")
      fdata = 0 if alist1 is None else alist1.data
      sdata = 0 if alist2 is None else alist2.data
      sum = carry + fdata+sdata 
      carry = 1 if sum>10 else 0 
      sum =sum if sum<10 else sum%10
      
      temp = Node(sum)
      
      if self.head is None:
        self.head = temp
      else:
        prev.head =temp
        
      prev= temp
      
      if alist1 is not None:
        alist1=alist1.next
      if alist2 is not None:
        alist2 = alist2.next
        
        
        
      if carry>0:
        temp.next = Node(carry)
        



alist1= LinkedList()
alist2=LinkedList()

for i in range(3):
  alist1.addData(int(input()))

#print(alist1.printl())
for i in range(3):
  alist2.addData(int(input()))

#print(first.printl())
#print(alist2.printl())

third = LinkedList()
third.addtwoList(alist1.head,alist2.head)
print(third.printl())


            
      
    
    