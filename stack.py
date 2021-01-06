#Stack Using LL

class Stack :
    #Define data members and __init__()
    '''----------------- Public Functions of Stack -----------------'''
    def __init__(self):
        self.head = None
        self.count = 0
    
    def getSize(self) :
        return self.count
    #Implement the getSize() function

    def isEmpty(self) :
        if self.head == None:
            return True
        else:
            return False
        #Implement the isEmpty() function

    def push(self, data) :
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
        self.count +=1
        #Implement the push(element) function
		
    def pop(self) :
        if self.head == None:
            return None
        else:
            nodedelete = self.head
            self.head = self.head.next
            nodedelete.next = None
            self.count -= 1
            return nodedelete.data
        
        #Implement the pop() function

    def top(self) :
        if self.head == None:
            return None
        else:
            return self.head.data        
	#Implement the top() function

# Stack using array

arr = []

######push
arr.insert(0,data)

##### pop
arr.pop(0)

####top
arr[0]
	
	
##########################Balanced Paranthesis


def isBalanced(expr):
    s=[]
    for char in expr:
        if char in '({[':
            s.append(char)
        elif char is ')':
            if (not s or s[-1]!="("):
                return False
            s.pop()
        elif char is '}':
            if (not s or s[-1]!="{"):
                return False
            s.pop()
        elif char is ']':
            if (not s or s[-1]!="["):
                return False
            s.pop()
    if not s:
        return True
    return False


######################Check redundant brackets

# Input: 
# ((a+b))
# (a+(b)/c)
# (a+b*(c-d))
# Output: 
# Yes
# Yes
# No

# Explanation:
# 1. ((a+b)) can reduced to (a+b), this Redundant
# 2. (a+(b)/c) can reduced to (a+b/c) because b is
# surrounded by () which is redundant.
# 3. (a+b*(c-d)) doesn't have any redundant or multiple
# brackets.

def checkRedundantBrackets(expression) :
    
    l1 = []
    
    for i in expression:
        if i != ')':
            l1.append(i)
        else:
            count = 0
	
	###while loop is to check this condition () and  (a) ie count no of elements between '(' and ')'
            while l1[-1] != '(':
                count += 1
                l1.pop()
            if count == 0 or count == 1:
                return True
            if count != 0 or count !=1:
                l1.pop()
		
    return False   
    
    ################# Reverse Stack
    arr = [1,2,3,4,5,6]
    #1. arr[::-1]

#2   i = 0
# while i!=len(arr):
#     arr.insert(i,arr.pop())
#     i+=1    
    
#### 3 

arr = []
s is string
###push in stack
for i in range(len(s)):
	arr.append(s[i])
	
rev = ""
while len(arr)!= 0:
	rev += arr.pop()
	
	


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ################  Stock Span
	
Stock Span
Send Feedback
Afzal has been working with an organization called 'Money Traders' for the past few years. The organization is into the money trading business. His manager assigned him a task. For a given array/list of stock's prices for N days, find the stock's span for each day.
The span of the stock's price today is defined as the maximum number of consecutive days(starting from today and going backwards) for which the price of the stock was less than today's price.
For example, if the price of a stock over a period of 7 days are [100, 80, 60, 70, 60, 75, 85], then the stock spans will be [1, 1, 1, 2, 1, 4, 6].
Explanation:
On the sixth day when the price of the stock was 75, the span came out to be 4, because the last 4 prices(including the current price of 75) were less than the current or the sixth day's price.

Similarly, we can deduce the remaining results.
Afzal has to return an array/list of spans corresponding to each day's stock's price. Help him to achieve the task.
Input Format:
The first line of input contains an integer N, denoting the total number of days.

The second line of input contains the stock prices of each day. A single space will separate them.
Output Format:
The only line of output will print the span for each day's stock price. A single space will separate them.
Note:
You are not required to print the expected output explicitly. It has already been taken care of. 
Constraints:
0 <= N <= 10^7
1 <= X <= 10^9
Where X denotes the stock's price for a day.

Time Limit: 1 second
Sample Input 1:
4
10 10 10 10
Sample Output 1:
1 1 1 1 
Sample Input 2:
8
60 70 80 100 90 75 80 120
Sample Output 2:
1 2 3 4 1 1 2 8 

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
	return len(stack) == 0
#Takes a list as a stack and returns the element at the top
def top(stack) :
#assuming the stack is never empty
	return stack[len(stack) - 1]
    
def stockSpan(price, n) :
	stk = list()
	output = [-1] * n
	stk.append(0)
	output[0] = 1
	for i in range(1, n) :
		while (not isEmpty(stk)) and (price[top(stk)] < price[i]) :
			stk.pop()
		
		if isEmpty(stk) :
			output[i] = i + 1
		else :
			output[i] = i - top(stk)
		stk.append(i)
	return output
    
    


######################alt sol   
    
def stockspan(price,n):
	lst=[]
	if len(price)>1:
		lst.append(1)

	for i in range(1,n):
		j=i-1
		count=1
		#######moving backward to count no of price less than crt price
		while j>-1 and price[i] > price[j]:
			count+=1
			j-=1
		
		lst.append(count)
    
    

    
    ###################  Minimum bracket Reversal
	
	
Minimum bracket Reversal
Send Feedback
For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.
If the expression can't be balanced, return -1.
Example:
Expression: {{{{
If we reverse the second and the fourth opening brackets, the whole expression will get balanced. Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

Expression: {{{
In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and hence will not be able to make the expression balanced and the output will be -1.
Input Format :
The first and the only line of input contains a string expression, without any spaces in between.
Output Format :
The only line of output will print the number of reversals required to balance the whole expression. Prints -1, otherwise.
Note:
You don't have to print anything. It has already been taken care of.
Constraints:
0 <= N <= 10^6
Where N is the length of the expression.

Time Limit: 1sec
Sample Input 1:
{{{
Sample Output 1:
-1
Sample Input 2:
{{{{}}
Sample Output 2:
1

    
    
def countMinReversals(expr):  
  
    lenn = len(expr)  
  
    # length of expression must be even  
    # to make it balanced by using reversals.  
    if (lenn % 2 != 0) : 
        return -1
  
    # After this loop, stack contains  
    # unbalanced part of expression,   
    # i.e., expression of the form "...."  
    s = []  
    for i in range(lenn): 
        if (expr[i] =='}' and len(s)>0):  
  
            if (s[0] == '{') : 
                s.pop(0)  
            else: 
                s.insert(0, expr[i])  
        else: 
            s.insert(0, expr[i])  
      
    # Length of the reduced expression  
    # red_len = (m+n)  
    red_len = len(s)  
  
    # count opening brackets at the  
    # end of stack  
    n = 0
    while (len(s)and s[0] == '{') : 
            s.pop(0)  
            n += 1
  
    # return ceil(m/2) + ceil(n/2) which 
    # is actually equal to (m+n)/2 + n%2  
    # when m+n is even.  
    return (red_len // 2 + n % 2)

if __name__ == '__main__':  
  
    expr = "}}{{"
    print(countMinReversals(expr.strip()))  ===========> 2 
  

###############alt soln
  
  
  
def countMinReversals(expr):  
  
    lenn = len(expr)  
  
    # length of expression must be even  
    # to make it balanced by using reversals.  
    if (lenn % 2 != 0) : 
        return -1
  
    # After this loop, stack contains  
    # unbalanced part of expression,   
    # i.e., expression of the form "...."  
    s = []    
    for i in inputString:  
        if i == '}' and  len(l1)>0 :
            if l1[-1]=='{':
                l1.pop()
            else:
                l1.append(i)
        else:
            l1.append(i)
      
    # Length of the reduced expression  
    # red_len = (m+n)  
    red_len = len(s)  
  
    # count opening brackets at the  
    # end of stack  
    n = 0
    while len(l1) and l1[-1]=='{':
        l1.pop()
        n+=1
  
    # return ceil(m/2) + ceil(n/2) which 
    # is actually equal to (m+n)/2 + n%2  
    # when m+n is even.  
    return (red_len // 2 + n % 2)

if __name__ == '__main__':  
  
    expr = "}}{{"
    print(countMinReversals(expr.strip()))  ===========> 2 
  
  
  ###############alt soln
  
  def findMinInversions(exp):
 
    # if the expression has odd length, it cannot be balanced
    if len(exp) % 2:
        return float('inf')
 
    inversions = 0              # stores total inversions needed
    open = 0                    # stores total number of opening braces
 
    # traverse the expression
    for i in range(len(exp)):
 
        # if current character is an opening brace
        if exp[i] == '{':
            open = open + 1
 
        # if current character is a closing brace
        else:
            # if an opening brace is found before, close it
            if open:
                open = open - 1        # decrement opening brace count
            else:
                # invert the closing brace i.e. change '}' to '{'
                inversions = inversions + 1     # increment total inversions needed by 1
                open = 1                        # increment opening brace count
 
    # for N opened brace, we need exactly N/2 inversions
    return inversions + open // 2
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
