
Return Subsequences
Send Feedback
Given a string (lets say of length n), return all the subsequences of the given string.
Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain same as in the input string.
Note : The order of subsequences are not important.
Sample Input:
abc
Sample Output:
"" (the double quotes just signifies an empty string, don't worry about the quotes)
c 
b 
bc 
a 
ac 
ab 
abc 


def subsequences(string):
    #Implement Your Code Here
    if string == "":
        output = []
        output.append(string)
        return output
    
    smallerString  = string[1:]
    smalleroutput = subsequences(smallerString)
    
    output = []
    
    #original string remains 
    for sub in smalleroutput:
        output.append(sub)
    #new string also included
    for sub in smalleroutput:
        sub_with_first_char = string[0] + sub
        output.append(sub_with_first_char)
        
    return output
    

string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)


Return Keypad
Send Feedback
Given an integer n, using phone keypad find out all the possible strings that can be made using digits of input n.
Note : The order of strings are not important.
Input Format :
Integer n
Output Format :
All possible strings in different lines
Constraints :
1 <= n <= 10^6
Sample Input:
23
Sample Output:
ad
ae
af
bd
be
bf
cd
ce
cf
    
    
def getString(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"
    return " "
    


def keypad(n):
    #Implement Your Code Here
    # pass
    if n == 0:
        output = []
        output.append("")
        return output
    
    smallerNumber = n//10
    lastDigit = n%10
    
    smallerOutput = keypad(smallerNumber)
    
    output = []
        
    lastDigitString = getString(lastDigit)
        
    for sub in smallerOutput:
        for l in lastDigitString:
            withlastDigit =  sub + l
            output.append(withlastDigit)
        
    return output
    
    

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)



############## Printing the answer insted of returning
    
def fact(n,ans):
    if n==0:
        print(ans)
        return
    
    ans = n*ans
    fact(n-1,ans)
    
    
fact(5,1)  --(5,1)--(4,5) -- (3,20) -- (2,60) -- (1,120)-- (0,120) -->120
    
    
#### Mnimum in list
    
def minlist(l):
    
    if len(l)==0:
        return l[0]
    
    no = minlist(l[1:])
    return min(l[0],no)
    
    
def minList(l,minsofar=100000000):
    if len(l) == 0:
        print(minsofar)
        return
    minno = min(l[0],minsofar)  
    minList(l[1:],minno)
    
    
    
# Return subsets sum to K
# Send Feedback
# Given an array A of size n and an integer K, return all subsets of A which sum to K.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important.
# Input format :
# Line 1 : Integer n, Size of input array
# Line 2 : Array elements separated by space
# Line 3 : K 
# Constraints :
# 1 <= n <= 20
# Sample Input :
# 9 
# 5 12 3 17 1 18 15 3 17 
# 6
# Sample Output :
# 3 3
# 5 1
    
    
def printAllSubsetsRec(arr, n, v, sum) : 
  
    # If remaining sum is 0, then print all 
    # elements of current subset. 
    if (sum == 0) : 
        # v.sort()
        for value in v : 
            print(value, end=" ") 
        print() 
        return
      
  
    # If no remaining elements, 
    if (n == 0): 
        return
  
    # We consider two cases for every element. 
    # a) We do not include last element. 
    # b) We include last element in current subset. 
    printAllSubsetsRec(arr, n - 1, v, sum) 
    v1 = [] + v 
    v1.append(arr[n - 1]) 
    printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1]) 
  
  
# Wrapper over printAllSubsetsRec() 
def subsetsSumK(arr, n, sum): 
  
    v = [] 
    printAllSubsetsRec(arr, n, v, sum) 
  

    
    
    Return subset of an array
Send Feedback
Given an integer array (of length n), find and return all the subsets of input array.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
Note : The order of subsets are not important.
Input format :

Line 1 : Size of array

Line 2 : Array elements (separated by space)

Sample Input:
3
15 20 12
Sample Output:
[] (this just represents an empty array, don't worry about the square brackets)
12 
20 
20 12 
15 
15 12 
15 20 
15 20 12 


def subs(s):
    if len(s)==0:
        output=[]
        output.append(" ")
        return output
    
    smallerString=s[1:]
    smallerOutput=subs(smallerString)
    
    output=[]
    
    for sub in smallerOutput:
        output.append(sub)
    
    for sub in smallerOutput:
        subs_with_zeroth_char=s[0]+" "+sub
        output.append(subs_with_zeroth_char)
    
    return output
    
n=int(input())
arr = input().split()
out=subs(arr)
for s in out:
    print(s)
    
    
    
    
   
##################2 approach
    

def subset(arr):
    n=len(arr)
    if(n<=0):
        output=[[]]
        return output
    output=subset(arr[:n-1])
    outputLen=len(output)
    #output*=2 This copies the reference .we need shallow copies
    for i in range(0,outputLen):
        output.append(output[i].copy())
        output[outputLen+i].append(arr[n-1])
    return output
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
output=subset(arr)
for lst in output:
    for num in lst:
        print(num,end=' ')
    print()
