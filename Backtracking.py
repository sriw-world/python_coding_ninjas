Rat in Maze











N-Queens
Send Feedback
You are given N, and for a given N x N chessboard, find a way to place N queens such that no queen can attack any other queen on the chess board. A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens. You have to print all such configurations.
Input Format :
Line 1 : Integer N
Output Format :
One Line for every board configuration. 
Every line will have N*N board elements printed row wise and are separated by space
Note : Don't print anything if there isn't any valid configuration.
Constraints :
1<=N<=10
Sample Input 1:
4
Sample Output 1 :
0 1 0 0 0 0 0 1 1 0 0 0 0 0 1 0 
0 0 1 0 1 0 0 0 0 0 0 1 0 1 0 0 


def isSafe(row,col,board,n): 
  #Check vertically   
  i = row-1     
  while i>=0:    
    if board[i][col] == 1:  
      return False     
    i-=1         
  
  i=row-1
  j=col-1
  while i>=0 and j>=0:     
    if board[i][j] == 1:      
      return False    
    i-=1  
    j-=1     
  
  i=row-1
  j=col+1   
  while i>=0 and j<n:
    if board[i][j] == 1:
      return False       
    i-=1      
    j+=1        
  
  return True 


def printPathsHelper(board,n,row): 
  if row == n:     
    for i in range(n): 
      for j in range(n):      
        print(board[i][j],end= ' ')  
    
    print()      
    return
  
  for col in range(n): 
    if isSafe(row,col,board,n) is True:   
      board[row][col] = 1       
      printPathsHelper(board,n,row+1)  
      board[row][col] = 0    
  return    


def nQueen(n):   
  board = [[0 for i in range(n)] for j in range(n) ] 
  printPathsHelper(board,n,0)
  
  
n  =  int(input()) 
nQueen(n)

  





















Sudoku Solver
Send Feedback
Given a 9*9 sudoku board, in which some entries are filled and others are 0 (0 indicates that the cell is empty), you need to find out whether the Sudoku puzzle can be solved or not i.e. return true or false.
Input Format :
9 Lines where ith line contains ith row elements separated by space
Output Format :
 true or false
Sample Input :
9 0 0 0 2 0 7 5 0 
6 0 0 0 5 0 0 4 0 
0 2 0 4 0 0 0 1 0 
2 0 8 0 0 0 0 0 0 
0 7 0 5 0 9 0 6 0 
0 0 0 0 0 0 4 0 1 
0 1 0 0 0 5 0 8 0 
0 9 0 0 7 0 0 0 4 
0 8 2 0 4 0 0 0 6
Sample Output :
true





def  presentInRow(board,row,num):
  for  j  in  range(9):
    if  board[row][j]  ==  num:
      return  True
  return  False 

def  presentInCol(board,col,num):
  for  j  in  range(9):
    if  board[j][col]  ==  num:
      return  True
  return  False 

def  presentInBox(board,row,col,num):
  for  i  in  range(row,row+3):
    for  j  in  range(col,col+3):
      if  board[i][j]  ==  num:
        return  True
  return  False


def  isPossible(board,row,col,num):
  if(presentInRow(board,row,num)):
    return  False
  if(presentInCol(board,col,num)):
    return  False
  if(presentInBox(board,row-(row%3),col-(col%3),num)):
    return  False 
  return  True 




def  solveSudoku(board):
  row  =  -1 
  col  =  -1 
  flag  =  False 
  for  i  in  range(9):
    for  j  in  range(9):
      if  board[i][j]  is  0: 
        row  =  i 
        col  =  j 
        flag  =  True 
        break 
    if  flag  is  True:
      break
  if  row  ==  -1:
    return  True 
  
  for  num  in  range(1,10):
    if(isPossible(board,row,col,num)):
      board[row][col]  =  num 
      if(solveSudoku(board)  is  True): 
        return  True 
      board[row][col]  =  0 
  return  False 
  
  
board  =  [[  int(ele)  for  ele  in  input().split()  ]for  i  in  range(9)]
ans  =  solveSudoku(board) 
if  ans  is  True:
  print('true') 
else: 
  print('false')
    

  
  
  
  
