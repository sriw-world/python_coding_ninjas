
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
    

    
