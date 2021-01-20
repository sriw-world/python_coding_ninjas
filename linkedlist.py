# Length of LL

def length(head) :
    #Your code goes here
    ctr = 0
    while head is not None:
        ctr = ctr+1
        head = head.next
    return ctr
    
    
def lengthRecursive(head):

    if head == None:
        return 0
    
    return 1 + lengthRecursive(head.next)

# Print ith node

def printIthNode(head, i):
    ctr = 0
    while head:
        if i == ctr:
            print(head.data)
            break
        ctr+=1
        head = head.next
    return
    
# Delete node


def length(head) :
    #Your code goes here
    ctr = 0
    while head is not None:
        ctr = ctr+1
        head = head.next
    return ctr


def deleteNode(head, pos) :
    curr = head
    prev = None
    i = 0
    if pos >= length(head):
        return head
    
    if pos == 0:
        curr = curr.next
        head.next = None
        head = curr
        return head

    
    while i < pos:
        prev = curr
        curr = curr.next
        i = i+1

    prev.next = curr.next
    curr.next = None
    return head


def deleteNodeRec(head , pos) :
    if pos < 0 and pos >= length(head):
        return(head)
    
    if head == None:
        return None
    if pos == 0 :
        curr = head
        curr = curr.next
        head.next = None
        return curr
      
    newnode = deleteNodeRec(head.next,pos-1)
    head.next = newnode
    
    return head



# Find a Node in Linked List
# 
Sample Input 1 :
2
3 4 5 2 6 1 9 -1
5
10 20 30 40 50 60 70 -1
6
Sample Output 1 :
2
-1
Sample Input 2 :
1
3 4 5 2 6 1 9 -1
6
Sample Output 2 :
4
 Explanation for Sample Input 2 :
For the given singly linked list, considering the indices starting from 0, progressing in a left to right manner with a jump of 1, then the N = 6 appears at position 4.




def findNode(head, n):
	
    pos =0    
    curr = head
    if head == None:
        return -1
    
    while head != None:
        
        if head.data == n:
            return pos
        else:
            head = head.next
            pos = pos + 1
    
    if pos >= length(curr):
        return -1
    
    

AppendLastNToFirst
Send Feedback
You have been given a singly linked list of integers along with an integer 'N'. Write a function to append the last 'N' nodes towards the front of the singly linked list and returns the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space. 

The second line contains the integer value 'N'. It denotes the number of nodes to be moved from last to the front of the singly linked list.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
Output format :
For each test case/query, print the resulting singly linked list of integers in a row, separated by a single space.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
0 <= N < M
Time Limit: 1sec

Where 'M' is the size of the singly linked list.
Sample Input 1 :
2
1 2 3 4 5 -1
3
10 20 30 40 50 60 -1
5
Sample Output 1 :
3 4 5 1 2
20 30 40 50 60 10
Sample Input 2 :
1
10 6 77 90 61 67 100  -1
4
Sample Output 2 :
90 61 67 100 10 6 77 
 Explanation to Sample Input 2 :
We have been required to move the last 4 nodes to the front of the list. Here, "90->61->67->100" is the list which represents the last 4 nodes. When we move this list to the front then the remaining part of the initial list which is, "10->6->77" is attached after 100. Hence, the new list formed with an updated head pointing to 90.



########################sarthak 
def appendLastNToFirst(head, k) :
    
	h0 = head
	total = 0
	
	while (h0 != None):
        
		h0 = h0.next
		total += 1
    
	if total<k:
		return None
    
	current = head
	count = 1
    
	while (count < total - k  and current is not None):
		current = current.next
		count += 1
    
	NewNode = current
    
	while (current.next is not None):
		current = current.next
    
	current.next = head  #head --> None
	head = NewNode.next #head --- NewNode
	NewNode.next = None
        
	return head
    
    
    
    Eliminate duplicates from LL
Send Feedback
You have been given a singly linked list of integers where the elements are sorted in ascending order. Write a function that removes the consecutive duplicate values such that the given list only contains unique elements and returns the head to the updated list.
 Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and the only line of each test case or query contains the elements(in ascending order) of the singly linked list separated by a single space.
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
 Output format :
For each test case/query, print the resulting singly linked list of integers in a row, separated by a single space.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Time Limit: 1sec

Where 'M' is the size of the singly linked list.
Sample Input 1 :
1
1 2 3 3 4 3 4 5 4 5 5 7 -1
Sample Output 1 :
1 2 3 4 3 4 5 4 5 7 
Sample Input 2 :
2
10 20 30 40 50 -1
10 10 10 10 -1
Sample Output 2 :
10 20 30 40 50
10



######################sarthak 
def removeDuplicates(head) :
	
    if  head == None or head.next == None:
        return head
    
    t1 = head
    t2 = head.next
    
    while t2 != None : 
        if t1.data == t2.data:
            t2 = t2.next
            
        else:
            t1.next = t2
            t1 = t2
            t2 = t2.next
            
		
########alt code

def removeDuplicates(head) :
	
    if  head == None or head.next == None:
        return head
    
    t1 = head
    t2 = head.next
    
    while t2 != None : 
        if t1.data != t2.data:
            t2 = t2.next
	    t1 = t1.next
            
        else:
            while t1.data==t2.data and t2!=None:
		t2=t2.next
	   
            t1.next = t2
            t1 = t2
            t2 = t2.next

            
          
    
        
        
Print Reverse LinkedList
Send Feedback
You have been given a singly linked list of integers. Write a function to print the list in a reverse order.
To explain it further, you need to start printing the data from the tail and move towards the head of the list, printing the head data at the end.
Note :
You can’t change any of the pointers in the linked list, just print it in the reverse order.
 Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Constraints :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
Output format :
For each test case, print the singly linked list of integers in a reverse fashion, in a row, separated by a single space.

Output for every test case will be printed in a seperate line.
 Constraints :
1 <= t <= 10^2
0 <= M <= 10^3
Time Limit: 1sec

Where 'M' is the size of the singly linked list.
Sample Input 1 :
1
1 2 3 4 5 -1
Sample Output 1 :
5 4 3 2 1
Sample Input 2 :
2
1 2 3 -1
10 20 30 40 50 -1
Sample Output 2 :
3 2 1
50 40 30 20 10



def printReverse(head) :
	
    if head == None:
        return
    
    printReverse(head.next)
    print(head.data , end = " " )

    
    
    
    
    Palindrome LinkedList
Send Feedback
You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.
 Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First and the only line of each test case or query contains the the elements of the singly linked list separated by a single space.
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
 Output format :
For each test case, the only line of output that print 'true' if the list is Palindrome or 'false' otherwise.
 Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Time Limit: 1sec

Where 'M' is the size of the singly linked list.
Sample Input 1 :
1
9 2 3 3 2 9 -1
Sample Output 1 :
true
Sample Input 2 :
2
0 2 3 2 5 -1
-1
Sample Output 2 :
false
true
Explanation for the Sample Input 2 :
For the first query, it is pretty intuitive that the the given list is not a palindrome, hence the output is 'false'.




def isPalindrome(head) :
	
    if head == None or head.next == None:
        return True
    
    l1 = []
    while head != None:
    
    	l1.append(head.data)
    	head = head.next
    
    if l1 == l1[::-1]:
        return True
    else:
        return False
    
# Reverse LL (Recursive)


def reverseLinkedListRec(head) :
    if head == None or head.next == None:
        return head
    
    smallhead = reverseLinkedListRec(head.next)
    curr = smallhead
	####while loop to reach end of new linked list
    while curr.next != None:
        curr = curr.next
        
    curr.next = head
    head.next = None
    return smallhead




def reverse(head):
    
    if head == None or head.next == None:
        return head
    
	####require 3 variable prev,curr,next
    crt = head
    prev = None
    
    while crt != None:
        next = crt.next
        crt.next = prev
        prev = crt
        crt = next
        
    return prev



# Midpoint of Linked list

def midPoint(head) :
    
    if head == None or head.next == None:
        return head 
    
    slow = head
    fast = head
    
    while fast.next != None and fast.next.next != None:
        
        slow = slow.next
        fast = fast.next.next
    
    return slow


# Code : Merge Sort


def findMid(head) :
    if head is None :
        return None
    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None :
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(head1, head2):
    if(head1 is None):
        return head2
    if(head2 is None):
        return head1
    newHead, newTail = None, None

    if head1.data < head2.data :
        newHead = head1
        newTail = head1
        head1 = head1.next
    else :
        newHead = head2
        newTail = head2
        head2 = head2.next

    while head1 is not None and head2 is not None :
        if head1.data < head2.data :
            newTail.next = head1
            newTail = newTail.next
            head1 = head1.next
        else :
            newTail.next = head2
            newTail = newTail.next
            head2 = head2.next
    if head1 is not None :
        newTail.next = head1
    if head2 is not None :
        newTail.next = head2
        
    return newHead

def mergeSort(head) :
    if head is None or head.next is None :
        return head
    
    mid = findMid(head)
    half1 = head
    half2 = mid.next
    mid.next = None
    half1 = mergeSort(half1)
    half2 = mergeSort(half2)
    
    finalHead = merge(half1, half2)
    
    return finalHead


# Find a node in LL (recursive)
Given a singly linked list of integers and an integer n, find and return the index for the first occurrence of 'n' in the linked list. -1 otherwise.

def findNodeRec(head, n) :
	
    if head == None:
        return -1
    
    if head.data == n:
        return 0
    
    ans=findNodeRec(head.next, n)
    if ans==-1:
        return -1
    return 1+ans


Even after Odd LinkedList
Send Feedback
For a given singly linked list of integers, arrange the elements such that all the even numbers are placed after the odd numbers. The relative order of the odd and even terms should remain unchanged.
Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format:
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space. 
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format:
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.

Time Limit: 1sec
Sample Input 1 :
1
1 4 5 2 -1
Sample Output 1 :
1 5 4 2 
Sample Input 2 :
2
1 11 3 6 8 0 9 -1
10 20 30 40 -1
Sample Output 2 :
1 11 3 9 6 8 0
10 20 30 40


def evenAfterOdd(head) :
	headO,tailO = None,None
	headE,tailE = None,None
	while head != None:
		if head.data % 2 != 0 :
			if headO == None:
				headO = head
				tailO = head
			else:
				tailO.next = head
				tailO=tailO.next
		else:
			if headE == None:
				headE = head
				tailE = head
			else:
				tailE.next = head
				tailE=tailE.next
		head=head.next
	if tailO != None:
		tailO.next = None
	if tailE != None:
		tailE.next = None
	if headO == None:
		return headE
	if headO != None:
		tailO.next = headE
	return headO








Delete every N nodes
Send Feedback
You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes. Continue the same until the end of the linked list.
To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.
Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space.

The second line of input contains two integer values 'M,' and 'N,' respectively. A single space will separate them.
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= P <= 10^5
Where P is the size of the singly linked list.
0 <= M <= 10^5
0 <= N <= 10^5 

Time Limit: 1sec
Sample Input 1 :
1
1 2 3 4 5 6 7 8 -1
2 2
Sample Output 1 :
1 2 5 6
Sample Input 2 :
2
10 20 30 40 50 60 -1
0 1
1 2 3 4 5 6 7 8 -1
2 3
Sample Output 2 :
1 2 6 7
Explanation of Sample Input 2 :
For the first query, we delete one node after every zero elements hence removing all the items of the list. Therefore, nothing got printed.

For the second query, we delete three nodes after every two nodes, resulting in the final list, 1 -> 2 -> 6 -> 7.

def skipMdeleteN(head, M, N) :
    
    if head == None:
        return head
    
    if M == 0:
        return None
    
    curr = head
    
    while curr:
        
        for i in range(1,M):
            if curr == None:
                return
            curr = curr.next
            
        if curr == None:
            return head 
        
        t1 = curr.next
        
        for j in range(1,N+1):
            
            if t1 == None:
                break 
                
            t1 = t1.next
        
        curr.next = t1
        curr = t1
        
    return head
    
    
    
Swap two Nodes of LL
Send Feedback
You have been given a singly linked list of integers along with two integers, 'i,' and 'j.' Swap the nodes that are present at the 'i-th' and 'j-th' positions.




Sample Input 1 :
1
3 4 5 2 6 1 9 -1
3 4
Sample Output 1 :
3 4 5 6 2 1 9 
 Sample Input 2 :
2
10 20 30 40 -1
1 2
70 80 90 25 65 85 90 -1
0 6
 Sample Output 2 :
10 30 20 40 
90 80 90 25 65 85 70 

def swapNodes(head, i, j) :
    
    
    tmp1 = head
    tmp2 = head
    for i in range(0,i):
        tmp1 = tmp1.next
    for i in range(0,j):
        tmp2 = tmp2.next
    
    a = tmp1.data
    tmp1.data = tmp2.data
    tmp2.data = a
    
    return head




kReverse
Send Feedback
Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.
 'k' is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.
Example :
Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

For k = 3, you should return: 3 -> 2 -> 1 -> 4 -> 5

Sample Input 1 :
1
1 2 3 4 5 6 7 8 9 10 -1
4
Sample Output 1 :
4 3 2 1 8 7 6 5 10 9
Sample Input 2 :
2
1 2 3 4 5 -1
0
10 20 30 40 -1
4
Sample Output 2 :
1 2 3 4 5 
40 30 20 10 



def reverse(head):
    
    prev = None
    curr = head
    
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev
    

def kReverse(head, k) :
    
    h1 = head
    t1 = head
    
    if head == None:
        return head
    
    for i in range(1,k):
        
        if t1.next == None:
            break
        t1 = t1.next
    
    if t1.next !=None:
        h2 = t1.next
        t1.next = None
    
    ###Reverse
    newhead = reverse(h1)
    
    parthead = kReverse(h2, k)
    t1.next = parthead
    
    return newhead
    
	
	
	
	
	
############alt soln
def reverse(self, head, k): 
        current = head  
        next  = None
        prev = None
        count = 0 
          
        # Reverse first k nodes of the linked list 
        while(current is not None and count < k): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next 
            count += 1
  
        # next is now a pointer to (k+1)th node 
        # recursively call for the list starting 
        # from current. And make rest of the list as 
        # next of first node 
        if next is not None: 
            head.next = self.reverse(next, k) 
  
        # prev is new head of the input list 
        return prev 
        
# Bubble Sort (Iterative) LinkedList


    
    
