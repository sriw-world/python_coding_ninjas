Memoization - storing results of recursion and returning result of recursion if stored

def fibonacci(n):
  if n==0 or n==1:
    return n
   
  return fibonacci(n-1) + fibonacci(n-2)

through dp
Time complexity reduced from o(2^n) to o(n)


def fibonacciR(n,dp):
  if n==0 or n==1:
    return n
  
  if  dp[n-1]==-1:
    ans1 = fibonacciR(n-1,dp)
    dp[n-1] = ans1
  else:
    ans1 = dp[n-1]
  if dp[n-2] == -1:
    ans2 = fibonacciR(n-2,dp)
    dp[n-2] = ans2  
  else:
    ans2 = dp[n-2]
  
  ans = an1 + ans2
   
  return ans
 
n = int(input())
dp = [-1 for i in range(n+1)]
ans = fibonacciR(n,dp)
print(ans)



########iteratively

def fibonacciI(n):
  dp = [-1 for i in range(n+1)]
  dp[0]=0
  dp[1]=1
  i=2
  while i<=n:
    dp[i] = dp[i-1]+dp[i-2]
    i+=1
  return dp[n]
  
n = int(input())
ans = fibonacciI(n)
print(ans)






Min Steps To 1
Send Feedback
Given a positive integer 'n', find and return the minimum number of steps that 'n' has to take to get reduced to 1. You can perform any one of the following 3 steps:
1.) Subtract 1 from it. (n = n - ­1) ,
2.) If n is divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 ) ,
3.) If n is divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 ).  
Input format :
The first and the only line of input contains an integer value, 'n'.
Output format :
Print the minimum number of steps.
Constraints :
1 <= n <= 10 ^ 6

Time Limit: 1 sec
Sample Input 1 :
4
Sample Output 1 :
2 
Explanation of Sample Output 1 :
For n = 4
Step 1 :  n = 4 / 2  = 2
Step 2 : n = 2 / 2  =  1 
Sample Input 2 :
7
Sample Output 2 :
3
Explanation of Sample Output 2 :
For n = 7
Step 1 :  n = 7 ­- 1 = 6
Step 2 : n = 6  / 3 = 2 
Step 3 : n = 2 / 2 = 1 




import sys
sys.setrecursionlimit(10000000)


def countMinStepsToOne(n,dp) : 
    
    ans1,ans2,ans3 = 999999,999999,999999
    
    if n==1:
        return 0
    
    if dp[n] != -1 :
        return dp[n]
    
    ans1 = countMinStepsToOne(n-1,dp)
    
    if n%2 == 0:
        ans2 = countMinStepsToOne(n//2,dp)
    if n%3 == 0:
        ans3 = countMinStepsToOne(n//3,dp)
    
    dp[n] = 1 + min(ans1,ans2,ans3)
    
    return dp[n]
    
    
     


Minimum square to 1

## 3 

import math,sys
def minSquare(n):
  if n == 0:
    return 0
    
  ans = sys.maxsize
  root = int(math.sqrt(n))
  for i in range(1,root+1):
    currAns = 1 + minSquare(n-(i**2))
    ans = min(ans,currAns)

  return ans

n = int(input())
ans = minSquare(n)
print(ans)



imporrt math,sys

def minSquare(n,dp):
  dp [-1 for i in range(n+1)]
  dp[0] = 0
  
  for i in range(1,n+1):
    ans = sys.maxsize
    root = int(math.sqrt(i))
    for j in range(1,root+1):
      currAns = 1 + dp[i-j**2]
      ans = min(ans,currAns)
    dp[i] = ans
    
  return dp[n]
  
  
  
  
  
  
Longest Increasing Subsequence
Send Feedback
Given an array with N elements, you need to find the length of the longest subsequence in the given array such that all elements of the subsequence are sorted in strictly increasing order.
Input Format
The first line of input contains an integer N. The following line contains N space separated integers, that denote the value of elements of array.
Output Format
The first and only line of output contains the length of longest subsequence.
Constraints
1 <= N <= 10^3
Time Limit: 1 second
Sample Input 1 :
6
5 4 11 1 16 8
Sample Output 1 :
3
Sample Output Explanation
Length of longest subsequence is 3 i.e. (5,11,16) or (4,11,16).
Sample Input 2 :
3
1 2 2
Sample Output 2 :
2


def lis(arr): 
    n = len(arr)
    l = [1]*n
    
    for i in range(1,n):
        for j in range(0,i):
            if arr[j] < arr[i] and l[i] < l[j] + 1:
                l[i] = l[j] + 1
                
    
    return max(l)
        
