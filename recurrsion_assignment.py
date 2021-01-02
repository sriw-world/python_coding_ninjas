Staircase
Send Feedback
A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
Input format :
Integer N
Output Format :
Integer W
Constraints :
1 <= N <= 30
Sample Input 1 :
4
Sample Output 1 :
7
Sample Input 2 :
5
Sample Output 2 :
13

def staircase(n):
  if(n<3):
    return n
  if(n==3):
    return 4 
  return staircase(n-1)+staircase(n-2)+staircase(n-3)
  
n=int(input())
count=staircase(n) print(count)




Check AB
Send Feedback
Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.
Input format :
String S
Output format :
'true' or 'false'
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
abb
Sample Output 1 :
true
Sample Input 2 :
abababa
Sample Output 2 :
false

def checkAB(str) :
  if(len(str) == 0):
    return True
  if(str[0] == 'a') :
    if(len(str[1:]) > 1 and str[1:3] == 'bb') :
      return checkAB(str[3:])
    else:
      return checkAB(str[1:])
  else :
    return False
    
str=input()
if(checkAB(str)):
  print("true")
else:
  print("false")
  
  
  
  
