class Node():
  
  def __init__(self,init_data):
    self.data = init_data
    self.next = None
    
  def setData(self, new_data):
    self.data = new_data
    
  def setNext(self,next_pos):
    self.next= next_pos
    
  def getData(self):
    return self.data
  
  def getNext(self):
    return self.next
    
class LinkedList():
  
  def __init__(self):
    self.head = None
    
  def addData(self,Data):
    temp = Node(Data)
    temp.setNext(self.head)
    self.head =temp
    
  def printAll(self):
    a=[]
    node = self.head
    while node!= None:
      a.append(node.getData())
      node=node.getNext() 
    return a
      
  def append(self,new_data):
    new_node= Node(new_data)
    if self.head == None:
      self.head = new_node
      return
    
    last = self.head
    
    while last.next:
      last=last.next
    
    last.next=new_node
    
  def between(self,prev_node, new_data):
    if prev_node == None:
      print("Need prev node to insert data")
      
    new_node = Node(new_data)
    
    new_node.next=prev_node.next
    prev_node.next = new_node
    
  def delete(self, key):
    
    temp = self.head
    
    if temp is not None:
      if temp.data ==key:
        self.head = temp.next
        temp = None
        
    while temp is not None:
      if temp.data == key:
        break
      prev=temp
      temp=temp.next
    
    if temp == None:
      return
    
    prev.next = temp.next
    temp = None
    
  def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            nexti = current.next
            current.next = prev
            prev = current
            current = nexti
        self.head = prev
        
  def sort(self):
    curr= self.head
    while curr is not None:
      a = curr.next
      b= curr.next.next
      if a.data>b.data:
        temo=curr.next
        curr.next=b
        b.next = a
    print (a)
  def sort(self):			#Bubble sort
    if self.head == None:
      print("There's nothing to sort!")
    if self.head == self.last:
      print("There's only one element in the list!")
    else:
      sorted = False
      count = 0
      while not sorted:
        sorted = True
        prev = self.head
        #print("self.head",self.head.getData())
        current = self.head.next
        while current != None:
          if prev.getData() > current.getData():
            sorted = False
            temp = prev.data
            prev.setData(current.getData())
            current.setData(temp)
            count += 1
            print("swap " + str(count) + ": ")
            print(" ")
          prev = current
          current = current.getNext()
	
      
	

ll3= LinkedList()
linklist1 = LinkedList()

linklist1.addData(12)
linklist1.addData(24)
#linklist1.printAll()
linklist1.append(36)
linklist1.between(linklist1.head.next,60)
#print(linklist1.head.getData(), "hi")
linklist1.addData(48)
#print(linklist1.head.getData(), "h")
#print(linklist1.printAll())
linklist1.delete(12)
print(linklist1.printAll( ), "hie")
linklist1.reverse()
#linklist1.printAll()
print(linklist1.printAll())

ll2 = LinkedList()

ll2.addData(3)
ll2.addData(4)
ll2.addData(7)
ll2.addData(90)

print(ll2.printAll())

ll2.sort()
print(ll2.printAll())