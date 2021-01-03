Geometric Sum
Send Feedback
Given k, find the geometric sum i.e.
1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
using recursion.
Input format :
Integer k
Output format :
Geometric sum (upto 5 decimal places)
Constraints :
0 <= k <= 1000
Sample Input 1 :
3
Sample Output 1 :
1.87500
Sample Input 2 :
4
Sample Output 2 :
1.93750

def geometric(n):
    
    if n==0:
        return 1/2**n
    
    return 1/2**n + geometric(n-1)






##############zeros count

def zeros_count(str):
    if len(str) == 0:
        return 0
    
    if str[0]=='0':
        return 1 + zeros_count(str[1:])
    else:
        return zeros_count(str[1:])
    
    
str = input()
count = zeros_count(str)
print(count)


# Check Palindrome (recursive)

function solve(str: string, start: integer, end: integer):
if(start >= end):
return true
if(str[start] != str[end]):
return false
return solve(str, start + 1, end - 1);
function checkPalindrome(str: a string):
return solve(str, 0, str.length() - 1);

# Sum of digits (recursive)

Sample Input 1 :
12345
Sample Output 1 :
15
Sample Input 2 :
9
Sample Output 2 :
9

def sumOfDigits(n):
# Write a recursive function that returns the sum of the digits of a given
# integer.
  if n == 0:
    return 0
  smallAns = sumOfDigits(n // 10)
  return smallAns + n%10


# Multiplication (Recursive) of 2 no

def multiplyNumbers(m, n):
  if m==0 or n==0:
    return 0
  if n>0:
    smallAns = multiplyNumbers(m,n-1)
    return smallAns + m
  else:
    smallAns = multiplyNumbers(m,n+1)
    return smallAns - m
  
  
  
  
Count Zeros
Send Feedback
Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
Input Format :
Integer N
Output Format :
Number of zeros in N
Constraints :
0 <= N <= 10^9
Sample Input 1 :
0
Sample Output 1 :
1
Sample Input 2 :
00010204
Sample Output 2 :
2
Explanation for Sample Output 2 :
Even though "00010204" has 5 zeros, the output would still be 2 because when you convert it to an integer, it becomes 10204.
Sample Input 3 :
708000
Sample Output 3 :
4



def countZeros(n):
  if n<0:
    n *= -1; # Make n positive
  if n<10:
    if n == 0:
      return 1
    return 0
  smallAns = countZeros(n // 10)
  if n%10==0:
    smallAns += 1
  return smallAn



String to Integer
Send Feedback
Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.
Input format :
Numeric string S (string, Eg. "1234")
Output format :
Corresponding integer N (int, Eg. 1234)
Constraints :
0 <= |S| <= 9
where |S| represents length of string S.
Sample Input 1 :
00001231
Sample Output 1 :
1231
Sample Input 2 :
12567
Sample Output 2 :
12567

int length(char input[])
{
int len = 0;
for (int i = 0; input[i] != '\0'; i++)
{
len++;
}
return len;
}
int stringToNumber(char input[], int last)
{
if (last == 0)
{
return input[last] - '0';
}
int smallAns = stringToNumber(input, last - 1);
int a = input[last] - '0';
return smallAns * 10 + a;
}
int stringToNumber(char input[])
{
int len = length(input);
return stringToNumber(input, len - 1);
}




Pair star
Send Feedback
Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
Input format :
String S
Output format :
Modified string
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
hello
Sample Output 1:
hel*lo
Sample Input 2 :
aaaa
Sample Output 2 :
a*a*a*a


int length(char input[])
{
int len = 0;
for (int i = 0; input[i] != '\0'; i++)
{
len++;
}
return len;
}
void pairStar(char input[], int start)
{
if (input[start] == '\0')
{
return;
}
pairStar(input, start + 1);
if (input[start] == input[start + 1])
{
int l = length(input);
input[l + 1] = '\0';
int i;
for (i = l - 1; i >= start + 1; i--)
{
input[i + 1] = input[i];
}
input[i + 1] = '*';
}
}




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
  
  
  
  
