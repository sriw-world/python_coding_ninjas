############# Print Tree
def printtree(root):
  ####edge cae
  if root==None:
    return
  print(root.data)
  #####if no child no execution of for loop so no base case reqd
  for child in root.children:  
    printtree(child)

#########print tree level wise

def printtree(root):
  ####edge cae
  if root==None:
    return
  print(root.data,":",end="")
  for child in root.children:  
    print(child.data,",",end="")
   
   print()
  #####if no child no execution of for loop so no base case reqd
  for child in root.children:  
    printtree(child)
    
    
def printLevelWiseTree(tree):
  q = [tree]
  while q:
    parent = q.pop(0)
    print(parent.data,':', ",".join(str(num) for num in parent.children),sep='')
    for child in parent.children:
      q.append(child)

#################Taking input in Generic Tree
def takeTreeInput(root):
  print("Enter root data")
  rootdata=int(input())
  if rootdata == -1:
    return None
    
  root =  Treenode(rootdata)
  print("Enter no of children for ",rootdata)
  childcount = int(input())
  for i in range(childcount):
    child = taketreeinput()
    root.children.append(child)
  return root
  
  
  
  
  ############ No of nodes in generic tree
  
  def numnodes(root):
    count = 0
    ### Edge case when no root is  passed
    if root == None:
      return count
    count += 1
    for child in root.children:
      count += numnodes(child)
      
    return count 
  
  ############### Sum of all nodes
  
def sumofNodes(tree):
    sum = 0
    if tree == None:
        return sum
    
    sum += tree.data
    
    for child in tree.children:
        sum += sumofNodes(child)
    
    return sum
    
    
    #################height of a generic tree
    
    def height(root):
    if root == None:
        return 0
    ht = 0
    for child in root.children:
        ht = max(ht,height(child))
    
    return 1 + ht

    
    
    ############ Node With Largest Data
    def maxDataNode(tree):
    maxnode = -1
    if tree == None:
        return -1
    maxm = tree.data
    for child in tree.children:
        maxm = max(maxm,maxDataNode(child))
    return maxm


#########Take input level wise

import queue
def taketreeinputlevelwise():
  q=queue.Queue()
  print("Enter root")
  rootdata=int(input())
  if rootdata ==-1:
    return None
  
  root= TreeNode(rootdata)
  q.put(root)
  while not q.empty():
    curr_node = q.get()
    print("Enter no of children for ",curr_node.data)
    noofchildren = int(input())
    for i in  range(noofchildren):
      print("Enter child of",curr_node.data)
      childdata = int(input())
      child = TreeNode(childdata)
      curr_node.children.append(child)
      q.put(child)
      
      
      
###########contains X

Given a generic tree and an integer x, check if x is present in the given tree or not. Return true if x is present, return false otherwise.
Input format :
Line 1 : Integer x
Line 2 : Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
Output format :
true or false
Sample Input 1 :
40
10 3 20 30 40 2 40 50 0 0 0 0 
Sample Output 1 :
true
Sample Input 2 :
4
10 3 20 30 40 2 40 50 0 0 0 0 
Sample Output 2:
false


def containsX(tree, x):
    
    if tree == None:
        return False
    if tree.data == x:
        return True
    
    for child in tree.children:
        out = containsX(child, x)
        if out == True:
            return out
    
    return False
        
        
################# No of leaf Node       

Given a generic tree, count and return the number of leaf nodes present in the given tree.
Input format :
Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
Output Format :
Count of leaf nodes
Sample Input 1 :
10 3 20 30 40 2 40 50 0 0 0 0 
Sample Output 1 :
4

      
def leafNodeCount(tree):
    if tree == None:
        return 0
    
    if len(tree.children)==0:
        return 1
    
    leaf = 0
    
    for child in tree.children:
        leaf  += leafNodeCount(child)
    
    return leaf
    
    
    
    ##################  Node with maximum child sum
    
    Given a tree, find and return the node for which sum of data of all children and the node itself is maximum. In the sum, data of node itself and data of immediate children is to be taken.
Input format :
Line 1 : Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
Output format :
Node with maximum sum.
Sample Input 1 :
5 3 1 2 3 1 15 2 4 5 1 6 0 0 0 0
Sample Output 1 :
1


    def maxSumNode(tree):
    
    if tree == None:
        return None,0

    rootchildsum = tree.data
    
    for child in tree.children:
        rootchildsum += child.data
    
    maxsum = rootchildsum
    maxnode = tree
    
    for child in tree.children:
        node,sum = maxSumNode(child)
        
        if sum > rootchildsum:
            maxsum = sum
            maxnode = node
    
    return maxnode,maxsum
                    

####################### Structurally identical
  
  Given two Generic trees, return true if they are structurally identical i.e. they are made of nodes with the same values arranged in the same way.
Input format :
Line 1 : Tree 1 elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
Line 2 : Tree 2 elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
Output format :
true or false
Sample Input 1 :
10 3 20 30 40 2 40 50 0 0 0 0 
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output 1 :
true
Sample Input 2 :
10 3 20 30 40 2 40 50 0 0 0 0 
10 3 2 30 40 2 40 50 0 0 0 0
Sample Output 2:
false
  
  
  def isIdentical(tree1, tree2):
    if tree1 == None and tree2 == None:
        return True
    
    if len(tree1.children) != len(tree2.children):
        return False
    
    for child1,child2 in zip(tree1.children,tree2.children):
        if child1.data != child2.data:
            return False
            
    for child1,child2 in zip(tree1.children,tree2.children):
        out = isIdentical(child1,child2)
        if out == False:
            return False
    return True

########Replace with depth

In a given Generic Tree, replace each node with its depth value. You need to just update the data of each node, no need to return or print anything.
Input format :
Line 1 : Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
Sample Input 1 :
10 3 20 30 40 2 40 50 0 0 0 0 
Sample Output 1 : (Level wise, each level in new line)
0 
1 1 1 
2 2

def replacewithDepth(tree,i):
    if tree == None:
        return
    
    tree.data = i
    
    for child in tree.children:
        replacewithDepth(child,i+1)




Next larger
Send Feedback
Given a generic tree and an integer n. Find and return the node with next larger element in the Tree i.e. find a node with value just greater than n.
Return NULL if no node is present with the value greater than n.
Input Format :
Line 1 : Integer n
Line 2 : Elements in level order form separated by space (as per done in class). Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
Output Format :
Node with value just greater than n.
Sample Input 1 :
18
10 3 20 30 40 2 40 50 0 0 0 0 
Sample Output 1 :
20
Sample Input 2 :
21
10 3 20 30 40 2 40 50 0 0 0 0 
Sample Output 2:
30
    
def nextLargest(tree, n):
  ans = None
  if not tree:
    return ans
  if tree.data > n:
    ans = tree
  for child in tree.children:
    temp = nextLargest(child, n)
    if temp:
      if (not ans) or ans.data > temp.data:
        ans = temp
  return ans


#### alt soon

def nextLargest(tree, n):
  ans = 0
  if tree== None:
    return ans
  if tree.data > n:
    ans = tree
  for child in tree.children:
    ans = min(ans,nextLargest(child, n))
  
  return ans

