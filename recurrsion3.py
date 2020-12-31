
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
    
    for sub in smalleroutput:
        output.append(sub)
    
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


