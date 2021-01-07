################# Removing Leaf Node
def removeleaf(root):
  if root == None:
    return None
    
  if root.left == None and root.right == None:
    return None
    
  root.left = removeleaf(root.left)
  root.right = removeleaf(root.right)
  
  return root
  
###########mirror binary tree
# Mirror of a Tree: Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged. 

  def mirrorBinaryTree(root) :
    
    if root == None:
        return None
    
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right) 
    
    tmp = root.left
    root.left = root.right
    root.right = tmp
    
    
    
    ############alt soln
    
def mirrorBinaryTree(root) :
    
    if root == None:
        return None
    
    l=mirrorBinaryTree(root.left)
    r=mirrorBinaryTree(root.right)
    
    root.left = r
    root.right=l
    return root

########## Binary Tree Is Balanced

# Consider a height-balancing scheme where following conditions should be checked to determine if a binary tree is balanced.
# An empty tree is height-balanced. A non-empty binary tree T is balanced if:
# 1) Left subtree of T is balanced
# 2) Right subtree of T is balanced
# 3) The difference between heights of left subtree and right subtree is not more than 1.

Time complexity O(n^2) and O(nlogn)
For every node it is checkinh height

def height(root):
  if root==None:
    return 0
   return 1 + max(height(root.left),height(root.right))
   
   
def isbalanced(root):
  if root==None:
    return True
    
  lt = height(root.left)
  rt = height(root.right)
  
  if lt-rt>1 or rt-lt>1:
    return False
  
  leftbalanced = isbalanced(root.left)
  rightbalanced = isbalanced(root.right)
  
  if leftbalanced and rightbalanced:
    return True
  else:
    return False
    
    --2------
def getheightBalanced(root):
  if root==None:
    return 0,True
  
  lt,leftbalanced = getheightBalanced(root.left)
  rt,rightbalanced = getheightBalanced(root.right)
  
  h = 1 + max(lh,rh)
  if lt-rt>1 or rt-lt>1:
    return h,False
  
  if leftbalanced and rightbalanced:
    return h,True
  else:
    return h,False
    
################### Diameter of Binary Tree

# The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes. 
# The diameter of a tree T is the largest of the following quantities:

# the diameter of T’s left subtree.
# the diameter of T’s right subtree.
# the longest path between leaves that goes through the root of T (this can be computed from the heights of the subtrees of T)

-------1-------------------
def diameterOfBinaryTree(root) :
    if root==None:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)
    
    ldia = diameterOfBinaryTree(root.left)
    rdia = diameterOfBinaryTree(root.right) 
    
    return max(lheight+rheight+1,max(ldia,rdia))
    
def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))

-----------2----------

def diameter_height(node):
    if node is None:
        return 0, 0
    ld, lh = diameter_height(node.left)
    rd, rh = diameter_height(node.right)
    return max(lh + rh + 1, ld, rd), 1 + max(lh, rh)



###########LevelSize print of node in tree
Print Levelwise

# Example 2:
#           1
#        /     \
#       2       3
#     /   \       \
#    4     5       6
#         /  \     /
#        7    8   9
# Output for above tree should be
# 1
# 2 3
# 4 5 6
# 7 8 9<

def printLevelWise(root):
    if root is None:
        return
    q=queue.Queue()
    q.put(root)
    while q.qsize()!=0:
        p=q.get()
        print(p.data,end=":")
        if p.left:
            print("L:{}".format(p.left.data),end=",")
            q.put(p.left)
        elif p.left is None:
            print("L:"+""+"-1",end=",")
        if p.right:
            print("R:{}".format(p.right.data),end="")
            q.put(p.right)
        elif p.right is None:
            print("R:"+""+"-1",end="")        
        print()

########################Construct Tree Using Inorder and Preorder

Input Format:
The first line of input contains an integer N denoting the size of the list/array. It can also be said that N is the total number of nodes the binary tree would have.

The second line of input contains N integers, all separated by a single space. It represents the preorder-traversal of the binary tree.

The third line of input contains N integers, all separated by a single space. It represents the inorder-traversal of the binary tree.

# Sample Input 1:
# 7
# 1 2 4 5 3 6 7 
# 4 2 5 1 6 3 7 
# Sample Output 1:
# 1 
# 2 3 
# 4 5 6 7 
# Sample Input 2:
# 6
# 5 6 2 3 9 10 
# 2 6 3 9 5 10 
# Sample Output 2:
# 5 
# 6 10 
# 2 3 
# 9 

def buildTreePreOrder(preorder, inorder):
    if len(preorder) == 0:
        return None
        
        ##gind root
    rootData = preorder[0]
    root = BinaryTreeNode(rootData)
    i=0
    ## inorder
    while i < len(inorder) :
        if inorder[i] == rootData:
            leftin=inorder[0:i]
            rightin=inorder[i+1:]
            break
        i += 1
    l= len(leftin)
    ##preorder
    Lpre= preorder[1:l+1]
    Rpre= preorder[l+1:]
    leftSub= buildTreePreOrder(Lpre,leftin)
    rightSub= buildTreePreOrder(Rpre,rightin)
    
    # connect 
    root.left=leftSub
    root.right=rightSub
    return root
 

################################### Construct Tree Using Inorder and postorder

# Depth First Traversals:
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1

# Input Format:
# The first line of input contains an integer N denoting the size of the list/array. It can also be said that N is the total number of nodes the binary tree would have.

# The second line of input contains N integers, all separated by a single space. It represents the Postorder-traversal of the binary tree.

# The third line of input contains N integers, all separated by a single space. It represents the inorder-traversal of the binary tree.
# Output Format:
# The given input tree will be printed in a level order fashion where each level will be printed on a new line. 
# Elements on every level will be printed in a linear fashion. A single space will separate them.

# Sample Input 1:
# 7
# 4 5 2 6 7 3 1 
# 4 2 5 1 6 3 7 
# Sample Output 1:
# 1 
# 2 3 
# 4 5 6 7 
# Sample Input 2:
# 6
# 2 9 3 6 10 5 
# 2 6 3 9 5 10 
# Sample Output 2:
# 5 
# 6 10 
# 2 3 
# 9 



def buildTree(postOrder, inOrder, n) :
    if len(postOrder) == 0 :
        return None
        
        ##Find root data
    rootdata = postOrder[-1]
    root = BinaryTreeNode(rootdata)
        ###Find location in inorder
    rootdataindex = -1
    for i in range(len(inOrder)):
        if inOrder[i] == rootdata:
            rootdataindex = i
            break
                
    if rootdataindex == -1:
        return None
        
        #Find inorder
    leftinorder = inOrder[:rootdataindex]
    rightinorder = inOrder[rootdataindex+1:]
        
    lengthleftinorder = len(leftinorder)
        
        #find postorder
    leftpostorder = postOrder[:lengthleftinorder]
    rightpostorder = postOrder[lengthleftinorder:-1]
        
    leftchild = buildTree(leftpostorder, leftinorder, n)
    rightchild = buildTree(rightpostorder, rightinorder, n)
        
    root.left = leftchild
    root.right = rightchild
        
    return root
        
################Create & Insert Duplicate Node

    2
   / \
  1   3
is changed to…

       2
      / \
     2   3
    /   /
   1   3
  /
 1
And the tree

            1
          /   \
        2      3
      /  \
    4     5
is changed to




               1
             /   \
           1      3
          /      /
        2       3
      /  \
     2    5
    /    /
   4   5
  /   
 4    

def insertDuplicateNode(root):
    if root  == None:
        return None
    
    addrleft = root.left
    
    data = root.data
    newnode = BinaryTreeNode(data)
    root.left = newnode
    
    newnode.left = addrleft
    insertDuplicateNode(newnode.left)
    insertDuplicateNode(root.right)


###########Minimum and Maximum in the Binary Tree


MIN_VALUE = -9999999999
MAX_VALUE = 9999999999

def getMinAndMax(root) :
    minimum,maximum=INT_MAX,INT_MIN
    if root ==None:
        return minimum,maximum
    leftmin,leftmax=getMinAndMax(root.left)
    rightmin,rightmax=getMinAndMax(root.right)
    minimum=min(root.data,leftmin,rightmin)
    maximum=max(root.data,leftmax,rightmax)
    return minimum,maximum



################ Level order traversal

# Level order traversal
# Send Feedback
# For a given a Binary Tree of type integer, print it in a level order fashion where each level will be printed on a new line. Elements on every level will be printed in a linear fashion and a single space will separate them.
# Example:
# alt txt

# For the above-depicted tree, when printed in a level order fashion, the output would look like:

# 10
# 20 30 
# 40 50 60
# Where each new line denotes the level in the tree.
# Input Format:
# The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.
# Output Format:
# The given input tree will be printed in a level order fashion where each level will be printed on a new line. 
# Elements on every level will be printed in a linear fashion. A single space will separate them.
# Constraints:
# 1 <= N <= 10^5
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1 
# Sample Output 1:
# 10 
# 20 30 
# 40 50 60 
# Sample Input 2:
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# Sample Output 2:
# 8 
# 3 10 
# 1 6 14 
# 4 7 13 


def printLevelATNewLine(root):
    q = queue.Queue()
    if root == None:
        return None
    
    q.put(root)
    q.put(None)
    while not q.empty():
        p = q.get()
        if p == None:
            print()
            if q.empty():
                break
            q.put(None)
        else:
            print(p.data , end = " ")
            if p.left != None:
                q.put(p.left)
            if p.right != None:
                q.put(p.right)


########### Path Sum Root to Leaf

# Path Sum Root to Leaf
# Send Feedback
# For a given Binary Tree of type integer and a number K, print out all root-to-leaf paths where the sum of all the node data along the path is equal to K.
# Example:
# alt txt

# If you see in the above-depicted picture of Binary Tree, we see that there are a total of two paths, starting from the root and ending at the leaves which sum up to a value of K = 13.

# The paths are:
# a. 2 3 4 4
# b. 2 3 8

# One thing to note here is, there is another path in the right sub-tree in reference to the root, which sums up to 13 but since it doesn't end at the leaf, we discard it.
# The path is: 2 9 2(not a leaf)
#  Input Format:
# The first line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.

# The second line of input contains an integer value K.
# Output Format:
# Lines equal to the total number of paths will be printed. All the node data in every path will be printed in a linear fashion taken in the order they appear from top to down bottom in the tree. A single space will separate them all.
# Constriants:
# 1 <= N <= 10^5
# 0 <= K <= 10^8
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 second
# Sample Input 1:
# 2 3 9 4 8 -1 2 4 -1 -1 -1 6 -1 -1 -1 -1 -1
# 13
#  Sample Output 1:
# 2 3 4 4 
# 2 3 8
# Sample Input 2:
# 5 6 7 2 3 -1 1 -1 -1 -1 9 -1 -1 -1 -1
# 13
#  Sample Output 2:
# 5 6 2
# 5 7 1

# def rootToLeafPathsSumToK(root, k, lst):
#     if root is None:
#         return None
#     if root.left is None and root.right is None:
#         if root.data==k:
#             print(*lst,k)
#     lst.append(root.data)
#     rootToLeafPathsSumToK(root.left,k-root.data,lst)
#     rootToLeafPathsSumToK(root.right,k-root.data,lst)
#     lst.pop()

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToK(root, k, lst):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.data==k:
            print(*lst,k)
    lst.append(root.data)
    rootToLeafPathsSumToK(root.left,k-root.data,lst)
    rootToLeafPathsSumToK(root.right,k-root.data,lst)
    lst.pop()


#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
k = int(stdin.readline().strip())
rootToLeafPathsSumToK(root, k,[])

  
  ##########has sum or not
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        if root.left is None and root.right is None:
            if root.val==sum:
                return True
        
        left = self.hasPathSum(root.left,sum-root.val)
        right = self.hasPathSum(root.right,sum-root.val)
        
        if left or right:
            return True
        else:
            return False
                
  
######### Print nodes at distance k from node  


# Print nodes at distance k from node
# Send Feedback
# You are given a Binary Tree of type integer, a target node, and an integer value K.
# Print the data of all nodes that have a distance K from the target node. The order in which they would be printed will not matter.
# Example:
# For a given input tree(refer to the image below):
# 1. Target Node: 5
# 2. K = 2
# alt txt

# Starting from the target node 5, the nodes at distance K are 7 4 and 1.
# Input Format:
# The first line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.

# The second line of input contains two integers separated by a single space, representing the value of the target node and K, respectively.
# Output Format:
# All the node data at distance K from the target node will be printed on a new line.

# The order in which the data is printed doesn't matter.
# Constraints:
# 1 <= N <= 10^5
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# 3 1
# Sample Output 1:
# 9
# 6
# Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# 3 3
# Sample Output 2:
# 4
# 5

  
def nodesAtDistanceKHelper(root, target, k) :
    if root is None :
        return -1
    if root.data == target :
        nodesAtDistanceKDown(root, k)
        return 0

    leftD = nodesAtDistanceKHelper(root.left, target, k)
    if leftD != -1 :
        if (leftD + 1) == k :
            print(root.data)
        else :
            nodesAtDistanceKDown(root.right, k - leftD - 2)
        return 1 + leftD

    rightD = nodesAtDistanceKHelper(root.right, target, k);
    if rightD != -1 :
        if (rightD + 1) == k :
            print(root.data)
        else :
            nodesAtDistanceKDown(root.left, k - rightD - 2)
        return 1 + rightD
    return -1

def nodesAtDistanceKDown(root, k) :
    if root is None : 
        return
    if k == 0 :
        print(root.data)
        return
    nodesAtDistanceKDown(root.left, k - 1)
    nodesAtDistanceKDown(root.right, k - 1)

def nodesAtDistanceK(root, node, k) :
    nodesAtDistanceKHelper(root, node, k)



################## Identical tree

def identicalTrees(a, b): 
      
    # 1. Both empty 
    if a is None and b is None: 
        return True 
  
    # 2. Both non-empty -> Compare them 
    if a is not None and b is not None: 
        return ((a.data == b.data) and 
                identicalTrees(a.left, b.left)and
                identicalTrees(a.right, b.right)) 
      
    # 3. one empty, one not -- false 
    return False
    
    
    
    
    
    
def printLevelWiseTree(tree):
    q1=queue.Queue()
    q2=queue.Queue()
    q1.put(tree)
    while not q1.empty():
        while not q1.empty():
            parent=q1.get()
            print(parent.data,end=':')
            for i in range(len(parent.children)):
                if i==len(parent.children)-1:
                    print(parent.children[i],end='')
                else:
                    print(parent.children[i],end=',')
                q2.put(parent.children[i])
            print()
        q1,q2=q2,q1
