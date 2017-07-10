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
	self.last = None
    
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
    
  def delete(self, key):  #Deleting a node
    
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
    
  def reverse(self): # Reversing the list
        prev = None
        current = self.head
        while(current is not None):
            nexti = current.next
            current.next = prev
            prev = current
            current = nexti
        self.head = prev
        
  
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
		  
  def size(self):
    count =0
    curr = self.head
    while curr!=None:
      count = count+1
      curr = curr.getNext()
    return count
	
  def selectionsort(self,count):   #Sorting only once
    if self.head == None:
      return self.head
    if self.head == self.last:
      return self.head
    else:
      sorted = False
      u=0
      ao=[]
      while u!=count:
        sorted = True
        prev= self.head
        curr = self.head.next
        
        while curr!=None:
          sorted = False
          print('c',curr.getData())
          print('p',prev.getData())
          if curr.getData() > prev.getData():
            prev=curr
            print(prev.getData(),'inside if')
            if curr.getNext()==None:
              break
            curr= curr.getNext()
            
          if curr.getNext() == None:
            break
          curr=curr.getNext()
          
        temp = prev.getData()
        prev.setData(curr.getData())
        curr.setData(temp)
        u=u+1
               
	
  def addLink(self,w,r):
    prev= None
    carry= 0
    temp = None
    
    while w is not None or r is not None:
        wdata = 0 if w is None else w.getData()
        rdata = 0 if r is None else r.getData()
        Sum = carry + rdata + wdata
        #print(Sum)
        
        carry = 1 if Sum>10 else 0 
        
        Sum = Sum if Sum<10 else Sum%10
        
        temp = Node(Sum)
        
        if self.head is None:
          self.head = temp
        else:
          prev.next = temp
          
        prev =temp
        
        if w is not None:
          w=w.next
        if r is not None:
          r= r.next
          
        if carry>0:
          temp.next = Node(carry)
		  
  def printinReverese(self):   #printing in reverse using list
    curr = self.head
    lst=list()
    while curr!=None:
      lst.append(curr.getData())
      curr= curr.getNext()
    lst.reverse()
    return lst

  def detectloop(self):			#detecting loops if any in a linkedlist
    ptr1=self.head
    ptr2=self.head
    while ptr2 and ptr1 and ptr2.next:
      ptr1 = ptr1.next
      ptr2=ptr2.next.next
      
      if ptr1==ptr2:
        self.removeLoop(ptr1)
        
      return 1
      
    return 0

   def removeLoop(self,loop):  # Not sure if it is working or not
    ptr = self.head
    while(1):
      ptr11 = loop
      while(ptr11.next != a and ptr11.next!=ptr):
        ptr11=ptr11.next
        
      if ptr11 ==a:
        break
      ptr = ptr.next
      
    ptr11.next = None	
	
	
	
	
  # def mergeList(self,a,b):
  #   curr = a
  #   q=[]
  #   while curr!=None:
  #     if curr.getData() not in q:
  #       q.append(curr.getData())
  #       #print(q)
  #     if curr.next == None:
  #       break
  #     curr=curr.next
  #     #print(curr.getData())    FAILED ATTEMPT
  #   print(q)
  #   f=[]
  #   curr2 = b
  #   while curr2!=None:
  #     if curr2.data not in f:
  #       f.append(curr2.data)
  #     #print(f)
  #     print(curr.data,'inside loop')
  #     curr.next =curr.setData(curr2.data)
  #     if curr2.next == None:
  #       break
  #     curr2=curr2.next
    
  #   print(curr.data,'outside loop')
  #   return curr	
  
  
	
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