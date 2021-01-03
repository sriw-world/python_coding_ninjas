
# Remove X
# Send Feedback
# Given a string, compute recursively a new string where all 'x' chars have been removed.
# Input format :
# String S
# Output format :
# Modified String
# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string S. 
# Sample Input 1 :
# xaxb
# Sample Output 1:
# ab
# Sample Input 2 :
# abc
# Sample Output 2:
# abc
# Sample Input 3 :
# xx
# Sample Output 3:


# Problem: Remove x from string
def removeX(str): 
    if len(str) == 0:
        return str
    smallOutput = removeX(str[1:])
    if str[0] == 'x':
        return "" + smallOutput
    else:
        return str[0] + smallOutput

# Main
str = input()
print(removeX(str))



# Remove Duplicates Recursively
# Send Feedback
# Given a string S, remove consecutive duplicates from it recursively.
# Input Format :
# String S
# Output Format :
# Output string
# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string
# Sample Input 1 :
# aabccba
# Sample Output 1 :
# abcba
# Sample Input 2 :
# xxxyyyzwwzzz
# Sample Output 2 :
# xyzwz



# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(str):
    if len(str) == 0 or len(str) == 1:
        return str
    smallOutput = removeConsecutiveDuplicates(str[1:])
    if str[0] == smallOutput[0]:
        return smallOutput
    else:
        return str[0] + smallOutput
    

# Main
str = input().strip()
print(removeConsecutiveDuplicates(str))




##### #merge sort



Algorithm	Time Complexity	 
 	                Best	Average	Worst	 
Selection Sort	    Ω(n^2)	θ(n^2)	O(n^2)	 
Bubble Sort	        Ω(n)	θ(n^2)	O(n^2)	 
Insertion Sort	    Ω(n)	θ(n^2)	O(n^2)	 
Heap Sort	   Ω(n log(n)) θ(n log(n))	O(n log(n))	 
Quick Sort	   Ω(n log(n))	θ(n log(n))	O(n^2)	 
Merge Sort	   Ω(n log(n))	θ(n log(n))	O(n log(n))	 
Bucket Sort	      Ω(n+k)	θ(n+k)	O(n^2)	 
Radix Sort	       Ω(nk)	θ(nk)	O(nk)


def merge(a1,a2,arr):
    i = 0 
    j = 0
    k = 0
    while i<len(a1) and j<len(a2):
        if a1[i] <a2[j]:
            arr[k] = a1[i]
            i = i + 1
            k = k + 1
        else:
            arr[k] = a2[j]
            j = j + 1
            k = k + 1
            
    while i<len(a1):
        arr[k] = a1[i]
        i = i + 1
        k = k + 1
    while j<len(a2):
        arr[k] = a2[j]
        j = j + 1
        k = k + 1
    

def mergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr)//2
    a1 = arr[0:mid]
    a2 = arr[mid:]
    mergeSort(a1)
    mergeSort(a2)
    merge(a1,a2,arr)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)




# Program for Tower of Hanoi
# Difficulty Level : Medium
#  Last Updated : 08 Dec, 2020
# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 

# Only one disk can be moved at a time. 
#  Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
# No disk may be placed on top of a smaller disk. 
# Approach : 
 

# Take an example for 2 disks :
# Let rod 1 = 'A', rod 2 = 'B', rod 3 = 'C'.

# Step 1 : Shift first disk from 'A' to 'B'.
# Step 2 : Shift second disk from 'A' to 'C'.
# Step 3 : Shift first disk from 'B' to 'C'.

# The pattern here is :
# Shift 'n-1' disks from 'A' to 'B'.
# Shift last disk from 'A' to 'C'.
# Shift 'n-1' disks from 'B' to 'C'.



def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B') 
# A, C, B are the name of rods
