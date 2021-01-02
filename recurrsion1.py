#######Power Of A Number


def power(x,n):
    if n == 0:
        return 1
    smallOutput = power(x,n-1)
    return x * smallOutput

x,n = map(int,input().split())
print(power(x,n))

# Sum Of Array

def sumArray(arr,N):
    if len(arr)== 1:
        return arr[0]
    else:
        return arr[0]+sumArray(arr[1:], N) 

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr,len(arr)))


# Check Number in Array

def checkNumber(list, num):
    # Please add your code here
  if len(list) == 0:
    return False
  if list[0] == num:
    return True
  return checkNumber(list[1:],num)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')

#    First Index of Number - Question
# Send Feedback
# Given an array of length N and an integer x, you need to find and return the first index of integer x present in the array. Return -1 if it is not present in the array.
# First index means, the index of first occurrence of x in the input array.
# Do this recursively. Indexing in the array starts from 0.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : Integer x
# Output Format :
# first index or -1
# Constraints :
# 1 <= N <= 10^3
# Sample Input :
# 4
# 9 8 10 8
# 8
# Sample Output :
# 1 
    
    
def firstindex(arr,x,si = 0):
    l = len(arr)
    if si == l:
        return -1
    if arr[si] == x:
        return si
    else:
        return firstindex(arr,x,si+1)

N = int(input())
arr = [int(k) for k in input().split()]
x = int(input())
answer = firstindex(arr,x)
print(answer)




# Last Index Of Number Question
# Send Feedback
# Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
# Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
# You should start traversing your array from 0, not from (N - 1).
# Do this recursively. Indexing in the array starts from 0.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : Integer x
# Output Format :
# last index or -1
# Constraints :
# 1 <= N <= 10^3
# Sample Input :
# 4
# 9 8 10 8
# 8
# Sample Output :
# 3


def lastindex(arr,x,si):
    if si == -1:
        return -1
    if arr[si] == x:
        return si
    return lastindex(arr,x,si-1)

N=int(input())
arr = list(map(int,input().split()))
x=int(input())
l = len(arr)-1
answer = lastindex(arr,x,l)
print(answer)
