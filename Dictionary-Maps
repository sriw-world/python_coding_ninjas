






########### Print all words with frequency k
def kfreqwords(s,k):
  words=s.split()
  d={}
  for word in words:
    d[word]=d.get(word,0) + 1
    
  for word in d:
    if d[word]==k:
      print(word)
      
      
######## Maximum Frequency

Maximum Frequency
Send Feedback
You are given an array of integers that contain numbers in random order. Write a program to find and return the number which occurs the maximum times in the given input.
If two or more elements contend for the maximum frequency, return the element which occurs in the array first.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Output Format :
Most frequent element
Constraints :
0 <= N <= 10^8
Sample Input 1 :
13
2 12 2 11 12 2 1 2 2 11 12 2 6 
Sample Output 1 :
2
Sample Input 2 :
3
1 4 5
Sample Output 2 :
1

def maxFreq(l):
    d={}
    for i in l:
        d[i] = d.get(i,0) +1
    max=l[0]
    for i in l:
        if d[max] < d[i]:
            max=i
    return max

      
      
#### Pair Sum To 0

Pair Sum To 0
Send Feedback
Given a random integer array A of size N. Find and print the pair of elements in the array which sum to 0.
Array A can contain duplicate elements.
While printing a pair, print the smaller element first.
That is, if a valid pair is (6, -6) print "-6 6". There is no constraint that out of 5 pairs which have to be printed in 1st line. You can print pairs in any order, just be careful about the order of elements in a pair.
Input format :
Line 1 : Integer N (Array size)
Line 2 : Array elements (separated by space)
Output format :
Line 1 : Pair 1 elements (separated by space)
Line 2 : Pair 2 elements (separated by space)
Line 3 : and so on
Constraints :
0 <= N <= 10^4
Sample Input:
5
2 1 -2 2 3
Sample Output :
-2 2
-2 2
      
def pairSum0(l):
    #l.sort()
    d={}
    for i in l:
        d[i] = d.get(i,0) +1
        
    for  i in l:
        if i==0:
            for j in range(d[i]):
                print(i,i)
            d[i]=0        
        elif -i in l:
            freq = d[i]*d[-i]
            for j in range(freq):
                print(i,-i)
            
            d[i],d[-i]=0,0
            
In computer science, a Hash table or a Hashmap is a type of data structure that maps keys to its value pairs (implement abstract array data types). It basically makes use of a function that computes an index value that in turn holds the elements to be searched, inserted, removed, etc. This makes it easy and fast to access data. In general, hash tables store key-value pairs and the key is generated using a hash function.
            
################### How to insert in Map
each index has a Linked List

class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class Map:
  
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
        
    def size(self):
        return self.count
        
    def getBucketIndex(self, hc):
      return abs(hc)%self.bucketSize
      
    def insert(self, key, value):   # First task is to find the index
                                    # At the index, if same key is present then change the corresponding value of it
    # If same key is not present then create a new Node, make newNode.next = head, self.buckets[index] = newNode and 
    # increment the count of that bucket
    
    hc = hash(key)
    index = getBucketIndex(hc)
    head = self.buckets[index]
    
    while head is not None:
        if head.key == key:
            head.value = value
            return
        head = head.next
    
    newNode = MapNode(key,value)
    self.buckets[index] = newNode
    newNode.next = head
    self.count += 1
    
    
    
    
    
m = Map()
m.insert('Sar', 2)
print(m.size())
m.insert('Sam', 7)
print(m.size())
m.insert('Sar', 4)  # It hasn't inserted the new node of key 'Fazeel' instead it just changed the value for of that key
print(m.size())


O/P
1
2
2
    
    
############ Insert and delete in hash map

class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class Map:
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
        
    def size(self):
        return self.count
    
    def getBucketIndex(self,hc):
        return (abs(hc)%(self.bucketSize))
    
    def insert(self, key, value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return 
            head = head.next
        
        # After iterating the LL make head pointing at buckets
        head = self.buckets[index] 
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
    
    def search(self.key):
    
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
                return 
            head = head.next
            
        return None
        
    def delete(self.key):
  
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        prev = None
        while head is not None:
            curr = head
            if head.key == key:
                if prev == None:
                    self.buckets[index] = head.next
                    return
                else:
                    prev.next = head.next
                
                self.count -= 1
                return head.value            
            prev = head
            head = head.next
            
        return None
            
            
        
m = Map()
m.insert('Sar', 2)
print(m.size())

print(m.getValue('Sar'), "Got Value of Fazeel")
m.insert('Sam', 7)
print(m.size())
m.insert('Sar', 4)  # It hasn't inserted the new node of key 'Fazeel' instead it just changed the value for of that key
print(m.size())
print(m.getValue('Sar'), "Got Value of Fazeel")
print(m.getValue('Sam'), "Got Value of Usmani")
print(m.getValue('Sarrrr'))

print(m.remove('Sar'))
print(m.getValue('Sam'), "Got Value of Usmani")
    
        
        

1
2 Got Value of Sar
2
2
4 Got Value of Sar
7 Got Value of Sam
None
4
7 Got Value of Sam
      
    

    
class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class Map:
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
        
    def size(self):
        return self.count
    
    def getBucketIndex(self,hc):
        return (abs(hc)%(self.bucketSize))
    
    def rehash(self):
        temp = self.buckets
        self.buckets = [None for i in range(2*self.bucketSize)]
        self.bucketSize = 2*self.bucketSize
        self.count = 0     # However we're increasing at the time of insertion
        
        for head in temp:
            while head is not None:
                self.insert(head.key, head.value)
                head = head.next
    
    def loadFactor(self):
        return self.count/self.bucketSize
    
    def insert(self, key, value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return 
            head = head.next
        
        # After iterating the LL make head pointing at buckets
        head = self.buckets[index] 
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
        loadFactor = self.count/self.bucketSize    
        if loadFactor >= 0.7:
            self.rehash()
        
        
    def getValue(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
            
        return None
            
            
    def remove(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        prev = None
        while head is not None:
            if head.key == key:
                
                if prev == None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                    
                self.count -=1
                return head.value
            
            prev = head    
            head = head.next
            
        return None
        
        
        
        
        m = Map()

for i in range(10):
    m.insert('abc' + str(i), i + 1)
    print(m.loadFactor())

for i in range(10):
    print("abc" + str(i) + ":" , m.getValue('abc'+str(i)))
    
    
    
    
    
    
    
    
    
    Extract Unique characters
Send Feedback
Given a string, you need to remove all the duplicates. That means, the output string should contain each character only once. The respective order of characters should remain same.
Input format :
String S
Output format :
Output String
Constraints :
0 <= Length of S <= 10^8
Sample Input 1 :
ababacd
Sample Output 1 :
abcd
Sample Input 2 :
abcde
Sample Output 2 :
abcde


1------------

def uniqueChars(string):
    d = ""
    for i in string:
        if i not in d:
            d += i
    return d
    
# Main
string = input()
print(uniqueChars(string))

2----------------

# characters of a string. 
NO_OF_CHARS = 256

def printDistinct(str): 
  
    # Create an array of size 256 and  
    # count of every character in it 
    count = [0] * NO_OF_CHARS 
  
    # Count array with frequency of  
    # characters  
    for i in range (len(str)): 
        if(str[i] != ' '): 
            count[ord(str[i])] += 1
    n = i 
    # Print characters having count  
    # more than 0 
    for i in range(n): 
        if (count[ord(str[i])] == 1): 
            print (str[i], end = "") 
            



Longest Consecutive Sequence
Send Feedback
You are given an array of unique integers that contain numbers in random order. Write a program to find the longest possible sequence of consecutive numbers using the numbers from given array.
You need to return the output array which contains consecutive elements. Order of elements in the output is not important.
Best solution takes O(n) time.
If two sequences are of equal length then return the sequence starting with the number whose occurrence is earlier in the array.
Input Format :
Line 1 : Integer n, Size of array
Line 2 : Array elements (separated by space)
Constraints :
0 <= n <= 10^6
Sample Input 1 :
13
2 12 9 16 10 5 3 20 25 11 1 8 6 
Sample Output 1 :
8 
9 
10 
11 
12
Sample Input 2 :
7
3 7 2 1 9 8 41
Sample Output 2 :
7
8
9
Explanation: Sequence should be of consecutive numbers. Here we have 2 sequences with same length i.e. [1, 2, 3] and [7, 8, 9], but output should be [7, 8, 9] because the starting point of [7, 8, 9] comes first in input array.
Sample Input 3 :
7
15 24 23 12 19 11 16
Sample Output 3 :
15 
16

def longestConsecutiveIncreasingSequence(l):
    d={}
    for i in l:
        d[i] = 'T'
        
    start = 0
    b = []
    for i in l:
        if d[i] != 'F':
            d[i] = 'F'
            a = [i]
            j = i - 1
            while j in d :
                d[j] = 'F'
                a.append(j)
                j -= 1
            
            j = i + 1
            while j in d:
                d[j] = 'F'
                a.append(j)
                j += 1               
                
            if len(a) > len(b):
                b = a

            elif len(a) == len(b) :
                min_a = min(a)
                min_b = min(b)
                if l.index(min_a) < l.index(min_b):
                    b = a
    return b         



Pairs with difference K
Send Feedback
You are given with an array of integers and an integer K. Write a program to find and print all pairs which have difference K.
Take difference as absolute.
Input Format :
Line 1 : Integer n, Size of array
Line 2 : Array elements (separated by space)
Line 3 : K
Output format :
Print pairs in different lines (pair elements separated by space). In a pair, smaller element should be printed first.
(Order of different pairs is not important)
Constraints :
0 <= n <= 10^4
Sample Input 1 :
4 
5 1 2 4
3
Sample Output 1 :
2 5
1 4
Sample Input 2 :
4
4 4 4 4 
0
Sample Output 2 :
4 4
4 4
4 4
4 4
4 4
4 4



# def printPairDiffK(l, k):

def printPairDiffK(l, k):
    d = {}
    for i in l:
        d[i] = d.get(i,0) + 1
        
    for i in d:
        if k==0:
            freq = d[i]*(d[i]-1)//2
            for j in range(freq):
                print(i,i) 
        if i-k in d :
            freq = d[i]*d[i-k]
            for j in range(freq):
                print(min(i,i-k) , max(i,i-k))
        if i+k in d:
            freq = d[i]*d[i+k]
            for j in range(freq):
                print(min(i,i+k) , max(i,i+k))
    
        d[i] = 0
            

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(l, k)

Longest subset zero sum
Send Feedback
Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.
NOTE: You have to return the length of longest subarray .
Input Format :
Line 1 : Contains an integer N i.e. size of array

Line 2 : Contains N elements of the array, separated by spaces
Output Format
 Line 1 : Length of longest subarray 
Constraints:
0 <= N <= 10^8
Sample Input :
10 
 95 -97 -387 -435 -5 -70 897 127 23 284
Sample Output :
5



def subsetSum(l):
#Implement Your Code Here
    hash_map = {}
    
    max_len = 0
    curr_sum = 0
    
    for i in range(len(l)):
        curr_sum += l[i]
        if l[i] is 0 and max_len is 0:
            max_len = i + 1
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])     
        else:
            hash_map[curr_sum] = i
    return max_len       
    


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
finalLen= subsetSum(l)
print(finalLen)




