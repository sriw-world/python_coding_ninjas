
# Array Intersection
# Send Feedback
# You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively. You need to print their intersection; An intersection for this problem 
# can be defined when both the arrays/lists contain a particular value or to put it in other words, when there is a common value that exists in both the arrays/lists.
# Note :
# Input arrays/lists can contain duplicate elements.

# The intersection elements printed would be in the order they appear in the first sorted array/list(ARR1).


# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains an integer 'N' representing the size of the first array/list.

# The second line contains 'N' single space separated integers representing the elements of the first the array/list.

# The third line contains an integer 'M' representing the size of the second array/list.

# The fourth line contains 'M' single space separated integers representing the elements of the second array/list.
# Output format :
# For each test case, print the intersection elements in a row, separated by a single space.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^6
# 0 <= M <= 10^6

# Time Limit: 1 sec 
# Sample Input 1 :
# 2
# 6
# 2 6 8 5 4 3
# 4
# 2 3 4 7 
# 2
# 10 10
# 1
# 10
# Sample Output 1 :
# 2 3 4
# 10
# Sample Input 2 :
# 1
# 4
# 2 6 1 2
# 5
# 1 2 3 4 2
# Sample Output 2 :
# 1 2 2
# Explanation for Sample Output 2 :
# Since, both input arrays have two '2's, the intersection of the arrays also have two '2's. The first '2' of first array matches with the first '2' of the second array.
# Similarly, the second '2' of the first array matches with the second '2' if the second array.



def intersection(arr1, arr2, n, m) :
  arr1.sort()
  arr2.sort()
  i = 0 #pointer to iterate over arr1
  j = 0 #pointer to iterate over arr2
  while i < n and j < m :
    if arr1[i] == arr2[j] :
      print(arr1[i], end = " ")
      i += 1
      j += 1
    elif arr1[i] < arr2[j] :
      i += 1
    else :
      j += 1
      
      
      
Array Equilibrium Index
Send Feedback
For a given array/list(ARR) of size 'N,' find and return the 'Equilibrium Index' of the array/list.
Equilibrium Index of an array/list is an index 'i' such that the sum of elements at indices [0 to (i - 1)] is equal to the sum of elements at indices [(i + 1) 
to (N-1)]. One thing to note here is, the item at the index 'i' is not included in either part.
If more than one equilibrium indices are present, then the index appearing first in left to right fashion should be returned. Negative one(-1) if no such index is present.
Example:
Let's consider an array/list Arr = [2, 3, 10, -10, 4, 2, 9]  of size, N = 7.

There exist two equilibrium indices, one at 2 and another at 3.

At index 2, the sum of all the elements to the left, [2 + 3] is 5, and the elements to its right, [-10 + 4 + 2 + 9] is also 5. Hence index 2 is an equilibrium index 
according to the condition we want to achieve. Mind it that we haven't included the item at index 2, which is 10, to either of the parts.

Similarly, we can see at index 3, the elements to its left sum up to 15 and to the right, sum up to 15 either. 

Since index 2 comes early in the order, left to right, the answer would be 2.
Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains an integer 'N' representing the size of the first array/list.

The second line contains 'N' single space separated integers representing the elements of the array/list
Output Format :
For each test case, print the 'Equilibrium Index'.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^6

Time Limit: 1 sec 
Sample Input 1 :
1
5
1 4 9 3 2
Sample Output 1 :
2
Sample Input 2 :
2
3
1 4 6
3
1 -1 4
Sample Output 2 :
-1
2



def arrayEquilibriumIndex(arr, n) :
  rightSum, leftSum = 0, 0
  for i in range(n) :
    rightSum += arr[i]
  for i in range(n) :
    rightSum -= arr[i]
    if rightSum == leftSum :
      return i
    leftSum += arr[i]
  return -1


# 1 case not passing why???
# def arrayEquilibriumIndex(arr, n) :
#     #Your code goes here
    
#     for i in range(len(arr)-1):
#         if arr[:i]==arr[i+1:]:
#             return i
        
#     return -1


Find the Unique Element
Send Feedback
You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
You need to find and return that number which is unique in the array/list.
 Note:
Unique element is always present in the array/list according to the given condition.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.
Output Format :
For each test case, print the unique element present in the array.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^6

Time Limit: 1 sec
Sample Input 1:
1
7
2 3 1 6 3 6 2
Sample Output 1:
1
Sample Input 2:
2
5
2 4 7 2 7
9
1 3 1 3 6 6 7 10 7
Sample Output 2:
4
10

##########XOR works because freq of every other element is 2 and one element freq is 0:
##########SO xor of even freq element is zero and odd freq element remains same

# 2 4 7 2 7

#  00
# 100
# 111
#  10
# 111
# ____
# 100



def findUnique(arr, n) :
  XOR = 0
  for i in range(n) :
    XOR ^= arr[i]
  return XOR



Duplicate in array
Send Feedback
You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). Each number is present at least once. That is, if N = 5,
the array/list constitutes values ranging from 0 to 3, and among these, there is a single integer value that is present twice. You need to find and return that 
duplicate number present in the array.
Note :
Duplicate number is always present in the given array/list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.
Output Format :
For each test case, print the duplicate element in the array/list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^6

Time Limit: 1 sec
Sample Input 1:
1
9
0 7 2 5 4 7 1 3 6
Sample Output 1:
7
Sample Input 2:
2
5
0 2 1 3 1
7
0 3 1 5 4 3 2
Sample Output 2:
1
3


def findDuplicate(arr, n) :
  sumOfNminusTwoNaturalNumbers = 0
  for i in range(n - 1) :
    sumOfNminusTwoNaturalNumbers += i
  sumOfElements = 0
  for i in range(n) :
    sumOfElements += arr[i]
  return (sumOfElements - sumOfNminusTwoNaturalNumbers)



Pair sum in array

Sample Input 1:
1
9
1 3 6 2 5 4 3 2 4
7
Sample Output 1:
7
Sample Input 2:
2
9
1 3 6 2 5 4 3 2 4
12
6
2 8 10 5 -2 5
10
Sample Output 2:
0
2


 Explanation for Input 2:
Since there doesn't exist any pair with sum equal to 12 for the first query, we print 0.

For the second query, we have 2 pairs in total that sum up to 10. They are, (2, 8) and (5, 5).


def pairSum(arr, n, num) :
  arr.sort()
  
  startIndex = 0
  endIndex = (n - 1)
  
  numPair = 0
  
  while startIndex < endIndex :
  
    if arr[startIndex] + arr[endIndex] < num :
      startIndex += 1
    elif arr[startIndex] + arr[endIndex] > num :
      endIndex -= 1
    else :
      elementAtStart = arr[startIndex]
      elementAtEnd = arr[endIndex]
      if elementAtStart == elementAtEnd :
        totalElementsFromStartToEnd = (endIndex - startIndex) + 1
        numPair += (totalElementsFromStartToEnd * (totalElementsFromStartToEnd - 1) // 2)
        return numPair
      
      tempStartIndex = startIndex + 1
      tempEndIndex = endIndex - 1
      
      while (tempStartIndex <= tempEndIndex) and (arr[tempStartIndex] == elementAtStart) :
        tempStartIndex += 1
      while (tempEndIndex >= tempStartIndex) and (arr[tempEndIndex] == elementAtEnd) :
        tempEndIndex -= 1
      totalElementsFromStart = (tempStartIndex - startIndex)
      totalElementsFromEnd = (endIndex - tempEndIndex)
      numPair += (totalElementsFromStart * totalElementsFromEnd)
      startIndex = tempStartIndex
      endIndex = tempEndIndex
  
  return numPair




Triplet sum
Send Feedback
You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(s) in the array/list which sum to X.


Sample Input 1:
1
7
1 2 3 4 5 6 7 
12
Sample Output 1:
5
Sample Input 2:
2
7
1 2 3 4 5 6 7 
19
9
2 -5 8 -6 0 5 10 11 -3
10
Sample Output 2:
0
5


 Explanation for Input 2:
Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.

For the second query, we have 5 triplets in total that sum up to 10. They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) and (-6, 5, 11)


def tripletSum(arr, n, num) :
  arr.sort()
  numTriplets = 0;
  for i in range(n) :
    pairSumFor = num - arr[i]
    numPairs = pairSum(arr, (i + 1), (n - 1), pairSumFor)
    numTriplets += numPairs
  return numTriplets


def pairSum(arr, startIndex, endIndex, num) :
  numPair = 0
  while startIndex < endIndex :
    if arr[startIndex] + arr[endIndex] < num :
      startIndex += 1
    elif arr[startIndex] + arr[endIndex] > num :
      endIndex -= 1
    else :
      elementAtStart = arr[startIndex]
      elementAtEnd = arr[endIndex]
      if elementAtStart == elementAtEnd :
        totalElementsFromStartToEnd = (endIndex - startIndex) + 1
        numPair += (totalElementsFromStartToEnd * (totalElementsFromStartToEnd - 1) // 2)
        return numPair
    
      tempStartIndex = startIndex + 1
      tempEndIndex = endIndex - 1
      while (tempStartIndex <= tempEndIndex) and (arr[tempStartIndex] == elementAtStart) :
        tempStartIndex += 1
      while (tempEndIndex >= tempStartIndex) and (arr[tempEndIndex] == elementAtEnd) :
        tempEndIndex -= 1
      
      totalElementsFromStart = (tempStartIndex - startIndex)
      totalElementsFromEnd = (endIndex - tempEndIndex)
      numPair += (totalElementsFromStart * totalElementsFromEnd)
      startIndex = tempStartIndex
      endIndex = tempEndIndex
  return numPair



Rotate array
Send Feedback
You have been given a random integer array/list(ARR) of size N. Write a function that rotates the given array/list by D elements(towards the left).


Sample Input 1:
1
7
1 2 3 4 5 6 7
2
Sample Output 1:
3 4 5 6 7 1 2
Sample Input 2:
2
7
1 2 3 4 5 6 7
0
4
1 2 3 4
2
Sample Output 2:
1 2 3 4 5 6 7
3 4 1 2


void swapElements(int *input, int i, int j)
{
int temp = input[i];
input[i] = input[j];
input[j] = temp;
}
void reverse(int *input, int start, int end)
{
int i = start, j = end;
while (i < j)
{
swapElements(input, i, j);
i++;
j--;
}
}
void rotate(int *input, int d, int n)
{
if (d >= n && n != 0)
{
d = d % n;
}
else if (n == 0)
{
return;
}
reverse(input, 0, n - 1);
reverse(input, 0, n - d - 1);
reverse(input, n - d, n - 1);
}





