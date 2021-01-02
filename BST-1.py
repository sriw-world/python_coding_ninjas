###########Search In BST

def searchInBST(root, k):
    if root == None:
        return False
    if k==root.data:
        return True
    if k<=root.data:
        return searchInBST(root.left, k)
    elif k>root.data:
        return searchInBST(root.right, k)
     
     
############ Print Elements In Range K1 and K2

def elementsInRangeK1K2(root, k1, k2):
    
    if root == None:
        return 
    if root.data > k2:
        elementsInRangeK1K2(root.left, k1, k2)
    elif root.data < k1:
        elementsInRangeK1K2(root.right, k1, k2)
    else:
        elementsInRangeK1K2(root.left, k1, k2)
        print(root.data,end = " ")
        elementsInRangeK1K2(root.right, k1, k2)
        




############construct bst

# Construct BST
# Send Feedback
# Given a sorted integer array A of size n, which contains all unique elements. You need to construct a balanced BST from this input array. Return the root of constructed BST.
# Note: If array size is even, take first mid as root.
# Input format:
# The first line of input contains an integer, which denotes the value of n. The following line contains n space separated integers, that denote the values of array.
# Output Format:
# The first and only line of output contains values of BST nodes, printed in pre order traversal.
# Constraints:
# Time Limit: 1 second
# Sample Input 1:
# 7
# 1 2 3 4 5 6 7
# Sample Output 1:
# 4 2 1 3 6 5 7


def constructBST(lst):
    if len(lst)==0:
        return None
    if len(lst)%2!=0:
        mid  = len(lst)//2
    else:
        mid  = len(lst)//2-1
    root = BinaryTreeNode(lst[mid])
    
    left = constructBST(lst[:mid])
    right = constructBST(lst[mid+1:])
    
    root.left = left
    root.right = right

    return root
    
    
    
    ############check bst
    
     O(n^2)
     
     
    INT_MAX = 999999999
    INT_MIN = -999999999
    
    def maximun(root):
        if root==None:
            return INT_MIN
        left = maxmin(root.left)
        right = maxmin(root.right)
        return max(root.data,left,right) 
        
        
    def minimum(root):
        if root==None:
            return INT_MAX
        left = maxmin(root.left)
        right = maxmin(root.right)
        return  min(root.data,left,right)
        
    
    def checkbst(root):
        if root==None:
            return True
        leftmax = maximum(root.left)
        rightmin = minimum(root.right)
        if root.data > rightmax and root.data < leftmin:
            return False
            
        left = checkbst(root.left)
        right = chectbst(root.right)
        
        return left and right
        
            
        
def  checkbst(root):
    if root == None:
        return -9999999,999999,True
    
    maxleft,minleft,leftbst= checkbst(root.left)
    maxright,minright,rightbst= checkbst(root.right)
    
    isTreeBST = True
    minimum = min(root.data,minleft,minright)
    maximum = max(root.data,maxleft,maxright)
    
    if root.data > rightmax and root.data < leftmin:
        isTreeBST = False
    if not(leftbst) and not(leftbst):
        isTreeBST = False
    
    return maximum,minimum,isTreeBST
    
    
 
 def checkbst(root,minrange,maxrange):
    if root==None:
        return True
    
    if root.data < minrange and root.data>maxrange:
        return False
        
    leftcons=checkbst(root.left,minrange,root.data-1)
    rightcons=checkbst(root.left,root.data,maxrange)
    
    return leftcons and rightcons
    

