######################sum of nodes of binary tree

def getSum(root):
    if root == None:
        return 0
    leftnode = getSum(root.left)
    rightnode = getSum(root.right)
    return root.data + leftnode + rightnode

################## Preorder Binary Tree
def preOrder(root):
    if root == None:
        return
    
    print(root.data,end = " ")
    leftnode = preOrder(root.left)
    rightnode = preOrder(root.right)
    return 
    
    
################## Postorder Binary Tree
def postOrder(root):
    if root == None:
        return
    leftnode = postOrder(root.left)
    rightnode = postOrder(root.right)
    print(root.data,end=" ")
    return
    
    ###########largest node in tree
def Largest(root):
    if root == None:
        return -1
    leftnode = Largest(root.left)
    rightnode = Largest(root.right)
    maximum = max(root.data + leftnode + rightnode)
    return maximum
    


###########no of leaf node
def leaf(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    leftnode = leaf(root.left)
    rightnode = leaf(root.right)
    return leftnode + rightnode

################### Print nodes at depth k

def print(root,k):
    if root == None:
        return 
    if k == 0:
        print(root.data)
        return 
    leftnode =  print(root.left,k-1)
    rightnode =  print(root.right,k-1)
   
###################### Replace Node With Depth

def changeToDepthTree(root,k) :
    if root == None:
        return
	
    root.data = k
    leftnode =  changeToDepthTree(root.left,k+1)
    rightnode =  changeToDepthTree(root.right,k+1)
    
 ################Node present    
 def isNodePresent(root, x) :
    if root == None:
        return False
    
    if root.data == x:
        return True
    
    leftnode =  isNodePresent(root.left,x)
    rightnode =  isNodePresent(root.right,x)
    
    if leftnode == True or rightnode == True:
        return True
    else:
        return False

##################  Nodes without sibling    ie that has only 1 parent
 
def printNodesWithoutSibling(root) :
    if root == None:
        return
    
    if root.left != None and root.right == None :
        print(root.left.data,end = " ")
        
    if root.left == None and root.right != None :
        print(root.right.data,end =" ")
        
    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)

