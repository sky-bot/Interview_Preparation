class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
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
  
  
root1 = Node(3) 
insert(root1,Node(2)) 
insert(root1,Node(1)) 
insert(root1,Node(4))  

root2 = Node(3)
insert(root2,Node(1)) 
insert(root2,Node(2)) 
insert(root2,Node(4)) 
insert(root2,Node(5))

def printLevelOrder(root): 
    # Base Case 
    if root is None: 
        return
      
    # Create an empty queue for level order traversal 
    queue = [] 
  
    # Enqueue Root and initialize height 
    queue.append(root) 
  
    while(len(queue) > 0): 
        print (queue[0].val, end='\t') 
        node = queue.pop(0) 
 
        if node.left is not None: 
            queue.append(node.left) 

        if node.right is not None: 
            queue.append(node.right) 

  
print(printLevelOrder(root1))
print(printLevelOrder(root2))

def mergeTrees(root1, root2):
    result = merge(root1, root2)
    return result
        
def merge(root1, root2):
    if root1 and root2:
        root1.val += root2.val
    else:
        return root1 or root2
    root1.left = merge(root1.left, root2.left)
    root1.right = merge(root1.right, root2.right)

    return root1

mergeTrees(root1, root2)
print("root1:", printLevelOrder(root1))