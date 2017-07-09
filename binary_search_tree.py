class node:
  def __init__(self,key):
    self.val=key
    self.left=None
    self.right=None
    
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
 

def inorder(root):
    if root:
      inorder(root.left)
      print(root.val)
      inorder(root.right)
 
def postorder(root):
    if root:
      postorder(root.left)
      postorder(root.right)
      print(root.val)
 
def preorder(root):
    if root:
      print(root.val)
      preorder(root.left)
      preorder(root.right)
      


def minValueNode(node):
  current =node
  
  while current.left:
    current=current.left
    
  return current
  
def search(root,key):
  if root is None:
    return root
  
  if root.val <key:
    search(root.right,key)
    
  if root.val> key:
    search(root.left,key)
  
  if root.val ==key:
    print('Key exists')
  
  
  # if root.left is not None or root.right is not None:
  #   if root.val ==key:
  #     print('Key exists')
  #     return
  #   else:
  #     print('Key does not exist')
  #     return
  
  
def Delete(root,key):
  
  temp2 = search(root,key)
  if temp2 == 'Key exists':
    
    if root is None:
      return root
    if key<root.val:
      root.left = Delete(root.left,key)
    elif key>root.val:
      root.right = Delete(root.right,key)
      
    else:
      
      if root.left is None:
        temp=root.right
        root = None
        return temp
        
      if root.right is None:
        temp = root.left
        root = None
        return temp
      
      temp=minValueNode(root.right) # so that key replaces the node to be deleted and becomes parent for other children, if any.
      
      root.val=temp.val #copy the key
        
      root.right = Delete(root.right,temp.val) # delete the key which was used as parent node 
          
        #temp = Delete(root,key)
        
    return root
  else:
    print('Cannot Delete because node not present')

# def error():
#   print('Error')
 
a=node(36)
insert(a,node(5))
insert(a,node(15))
insert(a,node(53))
insert(a,node(500))
insert(a,node(4))
insert(a,node(17))

#print('preorder',preorder(a))
#print('inorder',inorder(a))
#print('postorder',postorder(a))

#Delete(a,5)
(Delete(a,54))
#print('5')
search(a,5)
#print(i)
print('54')
search(a,54)
# if i==True:
#   print('Found')
print(inorder(a))