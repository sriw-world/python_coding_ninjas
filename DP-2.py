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
