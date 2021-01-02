Min Cost Path Problem
Send Feedback
An integer matrix of size (M x N) has been given. Find out the minimum cost to reach from the cell (0, 0) to (M - 1, N - 1).
From a cell (i, j), you can move in three directions:
1. ((i + 1),  j) which is, "down"
2. (i, (j + 1)) which is, "to the right"
3. ((i+1), (j+1)) which is, "to the diagonal"
The cost of a path is defined as the sum of each cell's values through which the route passes.
 Input format :
The first line of the test case contains two integer values, 'M' and 'N', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

The second line onwards, the next 'M' lines or rows represent the ith row values.

Each of the ith row constitutes 'N' column values separated by a single space.
Output format :
Print the minimum cost to reach the destination.
Constraints :
1 <= M <= 10 ^ 2
1 <= N <=  10 ^ 2

Time Limit: 1 sec
Sample Input 1 :
3 4
3 4 1 2
2 1 8 9
4 7 8 1
Sample Output 1 :
13
Sample Input 2 :
3 4
10 6 9 0
-23 8 9 90
-200 0 89 200
Sample Output 2 :
76
Sample Input 3 :
5 6
9 6 0 12 90 1
2 7 8 5 78 6
1 6 0 5 10 -4 
9 6 2 -10 7 4
10 -2 0 5 5 7
Sample Output 3 :
18

from sys import stdin
MAX_VALUE = 2147483647

def minCostPathHelper(input, mRows, nCols, currRow, currCol) :
 
 if (currRow >= mRows) or (currCol >= nCols) :
  return MAX_VALUE
 if currRow == (mRows - 1) and currCol == (nCols - 1) :
  return input[currRow][currCol]
 downCost = minCostPathHelper(input, mRows, nCols, (currRow + 1), currCol)
 diagonalCost = minCostPathHelper(input, mRows, nCols, (currRow + 1), (currCol + 1))
 leftCost = minCostPathHelper(input, mRows, nCols, currRow, (currCol + 1))
 
 return input[currRow][currCol] + min(diagonalCost, downCost, leftCost)

def minCostPath(input, mRows, nCols) :
 if mRows == 0 :
  return MAX_VALUE
 return minCostPathHelper(input, mRows, nCols, 0, 0)









LCS - Problem
Send Feedback
Given two strings, S and T with lengths M and N, find the length of the 'Longest Common Subsequence'.
For a string 'str'(per se) of length K, the subsequences are the strings containing characters in the same relative order as they are present in 'str,' but not necessarily contiguous. Subsequences contain all the strings of length varying from 0 to K.
Example :
Subsequences of string "abc" are:  ""(empty string), a, b, c, ab, bc, ac, abc.
Input format :
The first line of input contains the string S of length M.

The second line of the input contains the String T of length N.
Output format :
Print the length of the 'Longest Common Subsequence'.
Constraints :
0 <= M <= 10 ^ 3
0 <= N <= 10 ^ 3

Time Limit: 1sec
Sample Input 1 :
adebc
dcadb
Sample Output 1 :
3
Explanation of the Sample Input 1 :
Both the strings contain a common subsequence 'adb', which is the longest common subsequence with length 3. 
Sample Input 2 :
ab
defg
Sample Output 2 :
0
Explanation of the Sample Input 2 :
The only subsequence that is common to both the given strings is an empty string("") of length 0.

def lcs(s, t) :
 m = len(s)
 n = len(t)
 subProblems = [[0] * (n + 1) for i in range((m + 1))]
'''
Since all the values in the subProblem matrix will be Zero,
we don't explicitly have to have to iterate over the first
row and column.
'''
 for currStart in range(1, (m + 1)) :
  for currEnd in range(1, (n + 1)) :
   if s[m - currStart] == t[n - currEnd] :
    subProblems[currStart][currEnd] = 1 + subProblems[currStart - 1][currEnd - 1]
   else :
    subProblems[currStart][currEnd] = max(subProblems[currStart - 1][currEnd], subProblems[currStart][currEnd - 1])
 
 return subProblems[m][n]



















0 1 Knapsack - Problem
Send Feedback
A thief robbing a store can carry a maximal weight of W into his knapsack. There are N items, and i-th item weigh 'Wi' and the value being 'Vi.' What would be the maximum value V, that the thief can steal?
Input Format :
The first line of the input contains an integer value N, which denotes the total number of items.

The second line of input contains the N number of weights separated by a single space.

The third line of input contains the N number of values separated by a single space.

The fourth line of the input contains an integer value W, which denotes the maximum weight the thief can steal.
Output Format :
Print the maximum value of V that the thief can steal.
Constraints :
1 <= N <= 20
1<= Wi <= 100
1 <= Vi <= 100

Time Limit: 1 sec
Sample Input 1 :
4
1 2 4 5
5 4 8 6
5
Sample Output 1 :
13
Sample Input 2 :
5
12 7 11 8 9
24 13 23 15 16
26
Sample Output 2 :
51


def knapsack(weights, values, n, maxWeight) :
 if (n == 0) or (maxWeight == 0) :
  return 0
 
 if weights[n - 1] > maxWeight :
  return knapsack(weights, values, n - 1, maxWeight)

 includeItem = values[n - 1] + knapsack(weights, values, n - 1, maxWeight - weights[n - 1])
 excludeItem = knapsack(weights, values, n - 1, maxWeight)

 return max(includeItem, excludeItem)




Matrix Chain Multiplication
Send Feedback
Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices. In other words, determine where to place parentheses to minimize the number of multiplications.
You will be given an array p[] of size n + 1. Dimension of matrix Ai is p[i - 1]*p[i]. You need to find minimum number of multiplications needed to multiply the chain.
Input Format:
The first line of input contains an integer, that denotes the value of n. The following line contains n+1 integers, that denote the value of elements of array p[].
Output Format:
The first and only line of output prints the minimum number of multiplication needed.
Constraints :
1 <= n <= 100
Time limit: 1 second
Sample Input 1:
3
10 15 20 25
Sample Output 1:
8000
Sample Output Explanation:
There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
If we multiply in order- A1*(A2*A3), then number of multiplications required are 15000.
If we multiply in order- (A1*A2)*A3, then number of multiplications required are 8000.
Thus minimum number of multiplications required are 8000. 


def mcm(p,n):
 n+=1
 m=[[sys.maxsize for i in range (0,n+1)] for j in range (0,n+1)]
 for i in range (1,n):
   m[i][i]=0
 
 for l in range (2,n):
   for i in range (1,n-l+1):
     j=i+l-1
     for k in range (i,j):
       q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
       if(q<m[i][j]):
         m[i][j]=q
  
  return m[1][n-1]
