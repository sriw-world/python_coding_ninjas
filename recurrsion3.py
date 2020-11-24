
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





