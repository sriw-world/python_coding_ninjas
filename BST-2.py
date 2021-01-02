# Find path in BST
# Send Feedback
# Given a BST and an integer k. Find and return the path from the node with data k and root (if a node with data k is present in given BST) in a list. Return empty list otherwise.
# Note: Assume that BST contains all unique elements.
# Input Format :
# The first line of input contains data of the nodes of the tree in level order form. The data of the nodes of the tree is separated by space. If any node does not have left or right child, take -1 in its place. Since -1 is used as an indication whether the left or right nodes exist, therefore, it will not be a part of the data of any node.   
# The following line of input contains an integer, that denotes the value of k.
# Output Format :
# The first line and only line of output prints the data of the nodes in the path from node k to root. The data of the nodes is separated by single space.
# Constraints:
# Time Limit: 1 second   
# Sample Input 1:
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# 2
# Sample Output 1:
# 2 5 8



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
        
    

    
    
    
# BST Class
# Send Feedback
# Implement the BST class which includes following functions -
# 1. search
# Given an element, find if that is present in BST or not. Return true or false.
# 2. insert -
# Given an element, insert that element in the BST at the correct position. If element is equal to the data of the node, insert it in the left subtree.
# 3. delete -
# Given an element, remove that element from the BST. If the element which is to be deleted has both children, replace that with the minimum element from right sub-tree.
# 4. printTree (recursive) -
# Print the BST in ithe following format -
# For printing a node with data N, you need to follow the exact format -
# N:L:x,R:y
# wherer, N is data of any node present in the binary tree. x and y are the values of left and right child of node N. Print the children only if it is not null.
# There is no space in between.
# You need to print all nodes in the recursive format in different lines.

    
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printHelper(self,root):
        if root == None:
            return 
        print(root.data,end=":")
        if root.left!=None:
            print("L:",end='')
            print(root.left.data,end=",")
        if root.right!=None:
            print("R:",end='')
            print(root.right.data,end='')
        
        print()
        self.printHelper(root.left)
        self.printHelper(root.right)
    	
    def printTree(self):
        return self.printHelper(self.root)
    
    def searchHelper(self,root,data):
        if root==None:
            return False
        
        if root.data == data:
            return True
        if root.data>=data:
            return self.searchHelper(root.left,data)
        else:
            return self.searchHelper(root.right,data)
        
    def search(self, data):
        return self.searchHelper(self.root,data)

    def insertHelper(self,root,data):
        if root==None:
            root = BinaryTreeNode(data)
            return root
        
        if root.data>=data :
            root.left = self.insertHelper(root.left,data)
            return root
        else:
            root.right = self.insertHelper(root.right,data)
            return root
        
    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root,data)       
      
    def min(self,root):
        if root==None:
            return 10000
        if root.left ==None:
            return root.data
        
        return self.min(root.left)
    
    
    def deleteHelper(self,root,data):
        if root == None:
            return False,None
        
        if root.data>data :
            deleted,newleftnode = self.deleteHelper(root.left,data)
            root.left =  newleftnode
            return deleted,root
        if root.data<data:
            deleted,newrightnode = self.deleteHelper(root,data)
            root.right =  newrightnode
            return deleted,root
        
        #root is leaf
        if root.left==None and root.right == None:
            return True,None
        
        # root has 1 child
        if root.left==None:
            return True,root.right
        
        if root.right==None:
            return True,root.left
        
        replacement = self.min(root.right)
        root.data = replacement
        deleted , newRightNode = self.deleteHelper(root.right,replacement)
        root.right = newRightNode
        return True , root
    

            
    def delete(self, data):
        deleted,newroot = self.deleteHelper(self.root,data)
        if deleted :
            self.numNodes -=1
        self.root = newroot
        return deleted
    
    def count(self):
        return self.numNodes

b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()
