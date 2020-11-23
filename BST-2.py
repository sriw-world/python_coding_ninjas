
############ Root to Node Path in Binary Tree (Not BST)

Root==NOne
root.data == element

if left side not node append 
if none go to right side

if right side not node append 
if none go to left side

def nodetorootpath(root,s):
  if root==None:
    return None
    
  if root.data==s:
    l=[]
    l.append(root.data)
    return l
    
  leftlist = nodetorootpath(root.left,s)
  rightlist = nodetorootpath(root.right,s)
  if leftlist != None:
    leftlist.append(root.data)
    return leftlist
  elif rightlist != None:
    rightlist.append(root.data)
    return rightlist
  else:
    return None
    
    
    
######### Root to Node Path in BST


def findPathBST(root,data):
    if root == None:
        return None
    
    if root.data == data:
        l=[]
        l.append(root.data)
        return l
    
    if root.data >= data:
        leftlist = findPathBST(root.left,data)
        if leftlist != None:
            leftlist.append(root.data)
            return leftlist

    if root.data < data:
        rightlist = findPathBST(root.right,data)
        if rightlist != None:
            rightlist.append(root.data)
            return rightlist
    else:
        return None
        
    
