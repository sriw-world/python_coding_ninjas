heap sort follow binary tree and heap property (min max)
insertion and deletion same as heap property

if there are n nodes then there are n/2 leaf nodes

Inplace Heap Sort
Send Feedback
Given an integer array of size n. Sort this array (in decreasing order) using heap sort.
Space complexity should be O(1).
Input Format :
Line 1 : Integer n, Array size
Line 2 : Array elements, separated by space
Output Format :
Array elements after sorting
Constraints :
1 <= n <= 10^6
Sample Input:
6 
2 6 8 5 4 3
Sample Output:
8 6 5 4 3 2


10 5 8 1 4 6 7
          10 
      5         8
    1   4     6    7
    
    7 nodes 7//2 -1 =2 
    loop n to 0
    
    
#Time complexity of heapify is O(Logn). Time complexity of createAndBuildHeap() is O(n) and overall time complexity of Heap Sort is O(nLogn).
    
## Read input as specified in the question.
## Print output as specified in the question.
def down_heapify(arr,i,n):
    
    parentIndex = i
    leftChildIndex = 2*parentIndex+1
    rightChildIndex = 2*parentIndex+2
    
    while leftChildIndex<n:
        minIndex = parentIndex
        if arr[minIndex]<arr[leftChildIndex]:
            minIndex = leftChildIndex
        if rightChildIndex < n and arr[minIndex]<arr[rightChildIndex]:
            minIndex = rightChildIndex
        if minIndex == parentIndex:
            break
        
        arr[minIndex],arr[parentIndex] = arr[parentIndex],arr[minIndex]
        parentIndex = minIndex
        leftChildIndex = 2*parentIndex+1
        rightChildIndex = 2*parentIndex+2
    
    return
        
    
def heapSort(arr):
    ##build the heap for non leaf nodes for every index
    n = len(arr)
    for  i in range(n//2-1,-1,-1):
        down_heapify(arr,i,n)
    ###Removing n elements from heap and put then in correct position  ie sorting 
    ######process
    swap brings smallest elemnt to last ie to last index n-1
    again heapify upto  n-2
    sawap brings smallest element to 2nd last position
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        down_heapify(arr,0,i)
	
    return

n = int(input())
arr = [int(i) for i in input().split()]
heapSort(arr)
#for decreasing order
for i in arr[::-1]:      ### only arr:  for increasing order
    print(i,end=" ")

    
    
    
import heapq    ####inbulit function to create heap
Min heap
li= [1,5,4,8,7,9,11]
heapq.heapify(li)
print(li)
---- 1,5,4,8,7,9,11
heapq.heappush(li,2)
----1,2,5,4,7,9,11,8

heapq.heappop(li)  
### 1   remove min element

print(li)
###2,5,4,8,7,9,11

heapq.heapreplace(li,6)  ### replace min element with 6 and heapify

print(li)   4,5,6,8,7,9,11


Max heap

heapq._heapify_max(li)
heapq._heappop_max(li)
heapq._heapreplace_max(li,6)
################go to 0 index , position of new element in array
heapq._siftdown_max(li,0,len(l1)-1)



K Smallest Elements
Send Feedback
You are given with an integer k and an array of integers that contain numbers in random order. Write a program to find k smallest numbers from given array. You need to save them in an array and return it.
Time complexity should be O(nlogk) and space complexity should be not more than O(k).
Order of elements in the output is not important.
Input Format :
Line 1 : Size of array (n)
Line 2 : Array elements (separated by space)
Line 3 : Integer k
Output Format :
k smallest elements
Sample Input 1 :
13
2 12 9 16 10 5 3 20 25 11 1 8 6 
4
Sample Output 1 :
5
3
2
1


import heapq

def kSmallest(lst, k):
    arr = lst[:k]
    heapq._heapify_max(arr)
    for i in lst[k:]:
        if arr[0]>i:
            heapq._heapreplace_max(arr,i)
        
    return arr

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
for ele in ans:
    print(ele)




K Largest Elements
Send Feedback
You are given with an integer k and an array of integers that contain numbers in random order. Write a program to find k largest numbers from given array. You need to save them in an array and return it.
Time complexity should be O(nlogk) and space complexity should be not more than O(k).
Order of elements in the output is not important.
Input Format :
Line 1 : Size of array (n)
Line 2 : Array elements (separated by space)
Line 3 : Integer k
Output Format :
k largest elements
Sample Input :
13
2 12 9 16 10 5 3 20 25 11 1 8 6 
4
Sample Output :
12
16
20
25




def kLargest(lst, k):
    
    arr = lst[:k]
    heapq.heapify(arr)
    for i in lst[k:]:
        if arr[0]<i:
            heapq.heapreplace(arr,i)
            
    return arr
    
    

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')




Check Max-Heap
Send Feedback
Given an array of integers, check whether it represents max-heap or not.
Return true or false.
Input Format :
Line 1 : An integer N i.e. size of the array
Line 2 : N integers which are elements of the array, separated by spaces
Output Format :
true if it represents max-heap and false if it is not a max-heap
Constraints :
1 <= N <= 10^5
1 <= Ai <= 10^5
Sample Input :
8
42 20 18 6 14 11 9 4
Sample Output :
true



def checkMaxHeap(lst):
    n= len(lst)
    #from where non leaf node starts to 0
    for i in range(n//2-1,-1,-1):
        
        if lst[i]<lst[2*i+1]:
            return False
	    ###right index within limits
        elif 2*i+2 <n and lst[i]<lst[2*i+2]:
            return False
    
    return True
    
    
    
    
    
Kth largest element
Send Feedback
Given an array A of random integers and an integer k, find and return the kth largest element in the array.
Try to do this question in less than O(nlogn) time.
Input Format :
Line 1 : An integer N i.e. size of the array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : An integer k
Output Format :
kth largest element
Input Constraints :
1 <= N, Ai, k <= 10^5
Sample Input 1 :
6
9 4 8 7 11 3
2
Sample Output 1 :
9
Sample Input 2 :
8
2 6 10 11 13 4 1 20
4
Sample Output 2 :
10



import heapq

def kthLargest(lst, k):
    
    arr = lst[:k]
    heapq.heapify(arr)
    for i in lst[k:]:
        if arr[0]<i:
            heapq.heapreplace(arr,i)
    return min(arr)

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)


