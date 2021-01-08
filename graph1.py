class Graph:
  def __init__(Self,nVertices):
    self.nVertices = nVertices
    self.adjMatrix = [[0 for i in range(nVertices)] for j in ranje(nVertices)]
    
    def addEdge(self,v1,v2):
      self.adjMatrix[v1][v2] = 1
      self.adjMatrix[v2][v1] = 1
      
    def removeEdge(self,v1,v2):
      if self.containsEdge(v1,v2) is False:
        return
      
      self.adjMatrix[v1][v2] = 0
      self.adjMatrix[v2][v1] = 0
      
    def containsEdge(self,v1,v2):
      return True if self.adjMatrix[v1][v2] > 0 else False
      
    def __str__(self):
      return str(self.adjMatrix)

g = Graph()
g.addEdge(0,1)
g.addEdge(0,3)

print(g)   ##############it will print adjency matrix



DFS  Depth First Search

Downward Print of all nodes

class Graph:
  def __init__(Self,nVertices):
    self.nVertices = nVertices
    self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self,v1,v2):
      self.adjMatrix[v1][v2] = 1
      self.adjMatrix[v2][v1] = 1
      
    def removeEdge(self):
      if self.containsEdge(v1,v2) is False:
        return
      
      self.adjMatrix[v1][v2] = 0
      self.adjMatrix[v2][v1] = 0
      
    def containsEdge(self,v1,v2):
      return True if self.adjMatrix[v1][v2] > 0 else False
    
    
    def __dfsHelper(self,sv,visited):
      print(sv)
      visited[sv] = True
      
      ##########print all vertices in dfs fashion ie all adjency Downward Print of all nodes
      for i in range(self.nVertices):
        if self.adjMatrix[sv][i] > 0 and visited[i] is False:
          self.__dfsHelper(i,visited)
    
    def dfs(self):
      ############# visited keeps track of all vertices that are visited or not
      visited = [False for i in range(self.nVertices]
      self.__dfsHelper(0,visited)
    
    
    def __str__(self):
      return str(self.adjMatrix)
g = Graph()
g.addEdge(0,1)
g.addEdge(0,3)
g.dfs()


BFS Breadth First Search   ie level order traversal of graph

Code : BFS Traversal
Send Feedback
Given an undirected and disconnected graph G(V, E), print its BFS traversal.
Note:
1. Here you need to consider that you need to print BFS path starting from vertex 0 only. 
2. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
3. E is the number of edges present in graph G.
4. Take graph input in the adjacency matrix.
5. Handle for Disconnected Graphs as well
Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains space separated two integers, that denote that there exists an edge between vertex a and b.
Output Format :
Print the BFS Traversal, as described in the task.
Constraints :
0 <= V <= 1000
0 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1
Time Limit: 1 second
Sample Input 1:
4 4
0 1
0 3
1 2
2 3
Sample Output 1:
0 1 3 2

######for levelorder traversal we use queue
                                      
import queue
class Graph:
    def __init__(self,nverteces):
        self.nverteces=nverteces
        self.adjmatrix=[[0 for i in range(nverteces)] for j in range(nverteces)]
    def addEdge(self,v1,v2):
        self.adjmatrix[v1][v2]=1
        self.adjmatrix[v2][v1]=1
    def removeEdge(self,v1,v2):
        if self.containEdge(v1,v2) is False:
            return
        self.adjmatrix[v1][v2]=0
        self.adjmatrix[v2][v1]=0
    def containEdge(self,v1,v2):
        return True if self.adjmatrix[v1][v2]>0 else False
    def BFShelper(self,sv,visited):
        q=queue.Queue()
        # if self.q.qsize()==0:
        #     return
        q.put(sv)
        # print(sv)
        visited[sv]=True
        while q.empty() is False:
            u = q.get()
            print(u, end = " ")
            for i in range(self.nverteces):
            	if self.adjmatrix[u][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
        #BFShelper(self,q.get(),visited)
    
    def BFS(self):
        visited=[False for i in range(self.nverteces)]
        #######also include disconnected graph case also
        ##vertex not covered is conveered through loop 
        for i in range(self.nverteces):
            if visited[i] is False:
                ##only cover connected graph one
                self.BFShelper(i, visited)
                
li = [int(x) for x in input().split()]
v = li[0]
e = li[1]
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()]
    g.addEdge(a, b)
g.BFS()




Code : Has Path
Send Feedback
Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), check if there exists any path between them or not. Print true if the path exists and false otherwise.
Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex 'a' and 'b'.
The following line contain two integers, that denote the value of v1 and v2.
Output Format :
The first and only line of output contains true, if there is a path between v1 and v2 and false otherwise.
Constraints :
0 <= V <= 1000
0 <= E <= 1000
0 <= a <= V - 1
0 <= b <= V - 1
0 <= v1 <= 2^31 - 1
0 <= v2 <= 2^31 - 1
Time Limit: 1 second
Sample Input 1 :
4 4
0 1
0 3
1 2
2 3
1 3
Sample Output 1 :
true
Sample Input 2 :
6 3
5 3
0 1
3 4
0 3
Sample Output 2 :
false


class graph:
    def __init__(self,n):
        self.nVertices=n
        self.adjMatrix=[[0 for i in range(n)] for j in range(n)]
        
    def addedge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
    def removeedge(self,v1,v2):
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def path(self,s,e,visited):
        
        if s>= self.nVertices or e>= self.nVertices:
            return False
        if self.adjMatrix[s][e] == 1:
            return True
        
        visited[s] = True
        
        for i in range(self.nVertices):
            if self.adjMatrix[s][i] > 0 and visited[i] is False:
                x=self.path(i,e,visited)
                if x is True:
                    return True
        return False
        

# #main
v,E=[int(x) for x in input().split()]
g=graph(v)
for i in range(E):
    v1,v2=[int(x) for x in input().split()]
    g.addedge(v1,v2)

s,e = [int(x) for x in input().split()]
visited = [False for i in range(v)]
out  = g.path(s,e,visited)
if out == True:
    print("true")
else:
    print("false")
    
    
    
Code : Get Path - DFS
Send Feedback
Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
Find the path using DFS and print the first path that you encountered.
Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
3. Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
4. Save the input graph in Adjacency Matrix.
Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex 'a' and 'b'.
The following line contain two integers, that denote the value of v1 and v2.
Output Format :
Print the path from v1 to v2 in reverse order.
Constraints :
2 <= V <= 1000
1 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1
0 <= v1 <= 2^31 - 1
0 <= v2 <= 2^31 - 1
Time Limit: 1 second
Sample Input 1 :
4 4
0 1
0 3
1 2
2 3
1 3
Sample Output 1 :
3 0 1
Sample Input 2 :
6 3
5 3
0 1
3 4
0 3
Sample Output 2 :

###########my solution

    def getpath(self,s,e,visited,l):
        
        if s>= self.nVertices or e>= self.nVertices:
            return []
        
                
        if s==e:
            return [s]
            
        if self.adjMatrix[s][e] == 1:
            l.append(e)
            l.append(s)
            return l
        
        visited[s] = True
        
        for i in range(self.nVertices):
            if self.adjMatrix[s][i] > 0 and visited[i] is False:
                x=self.getpath(i,e,visited,l)
                if len(x) != 0:
                    l.append(s)
                    return l
        return []



############# TA soln

from sys import stdin
## Read input as specified in the question.
## Print output as specified in the question.
from queue import Queue

class Graph:
    def __init__(self,num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adj_metrix = [[0 for i in range(num_of_vertices)] for i in range(num_of_vertices)]
    
   
    def addEdge(self,v1,v2):
        self.adj_metrix[v1][v2] = 1
        self.adj_metrix[v2][v1] = 1
       
    def removeEdge(self,v1,v2):
        if not self.isedge(v1,v2):
            return
        self.adj_metrix[v1][v2] = 0
        self.adj_metrix[v2][v1] = 0
       
    def isedge(self,v1,v2):
        return self.adj_metrix[v1][v2]
   
    def __str__(self):
        return str(self.adj_metrix)
   
    
    def __printpathdfs(self,v1,v2,isvisited):
        isvisited[v1] = 1
        if v1 == v2:
            return [v1]
        for i in range(self.num_of_vertices):
            if self.isedge(v1,i) and not isvisited[i]:
                isvisited[i] = 1
                ans = self.__printpathdfs(i,v2,isvisited)
                if ans:
                    ans.append(v1)
                    return ans
        return []
   
    def printpathdfs(self,v1,v2):

        isvisited = [0 for i in range(self.num_of_vertices)]
        return self.__printpathdfs(v1,v2,isvisited)

from sys import stdin
import sys
sys.setrecursionlimit(10**8)
a=stdin.readline().strip().split()
n=int(a[0])
m=int(a[1])
g=Graph(n)
li={}
for i in range(m):
    a=stdin.readline().strip().split()
    v1=int(a[0])
    v2=int(a[1])
    g.addEdge(v1,v2)
a=stdin.readline().strip().split()
v1=int(a[0])
v2=int(a[1])
s=g.printpathdfs(v1,v2)
if s!=None:
    for i in s:
        print(i,end=" ")
   



Code : Get Path - BFS
Send Feedback
Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
Find the path using BFS and print the shortest path available.
Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
3. Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
4. Save the input graph in Adjacency Matrix.
Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
The following line contain two integers, that denote the value of v1 and v2.
Output Format :
Print the path from v1 to v2 in reverse order.
Constraints :
2 <= V <= 1000
1 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1
0 <= v1 <= 2^31 - 1
0 <= v2 <= 2^31 - 1
Time Limit: 1 second
Sample Input 1 :
4 4
0 1
0 3
1 2
2 3
1 3
Sample Output 1 :
3 0 1
Sample Input 2 :
6 3
5 3
0 1
3 4
0 3
Sample Output 2 :


# Write your code 

import queue

class Graph:
    
    def __init__(self,n):
        self.nVertices=n
        self.adjMatrix=[[0 for i in range(n)] for j in range(n)]
        
    def addedge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
    def removeedge(self,v1,v2):
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def __getpathHelper(self,s,e,visited,q):
        
        if self.adjMatrix[s][e] > 0:
            return [e,s]
        
        q.put(s)
        visited[s] = True
        while q.empty() is False:
            u = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] > 0 and visited[i] is False and u!=i:
                    #q.put(i)
                    out = self.__getpathHelper(i,e,visited,q)
                    if len(out) != 0:
                        out.append(s)
                        return out
        return []
        
    def getpath(self,s,e):
        visited = [False for i in range(self.nVertices)]
        q = queue.Queue()
        
        if s==e:
            return [s]
        
        if s>= self.nVertices or e>= self.nVertices:
            return []
        
        return self.__getpathHelper(s,e,visited,q)
        

                
from sys import stdin
import sys
sys.setrecursionlimit(10**8)
a=stdin.readline().strip().split()
n=int(a[0])
m=int(a[1])
g=Graph(n)
li={}
for i in range(m):
    a=stdin.readline().strip().split()
    v1=int(a[0])
    v2=int(a[1])
    g.addedge(v1,v2)
a=stdin.readline().strip().split()
v1=int(a[0])
v2=int(a[1])
s=g.getpath(v1,v2)
if s!=None:
    for i in s:
        print(i,end=" ")
        
        
Code : Is Connected ?
Send Feedback
Given an undirected graph G(V,E), check if the graph G is connected graph or not.
Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
Output Format :
The first and only line of output contains "true" if the given graph is connected or "false", otherwise.
Constraints :
0 <= V <= 1000
0 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1
Time Limit: 1 second
Sample Input 1:
4 4
0 1
0 3
1 2
2 3
Sample Output 1:
true
Sample Input 2:
4 3
0 1
1 3 
0 3
Sample Output 2:
false 
Sample Output 2 Explanation
The graph is not connected, even though vertices 0,1 and 3 are connected to each other but there isn’t any path from vertices 0,1,3 to vertex 2. 

# Write your code 

import queue

class Graph:
    
    def __init__(self,n):
        self.nVertices=n
        self.adjMatrix=[[0 for i in range(n)] for j in range(n)]
        
    def addedge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
    def removeedge(self,v1,v2):
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def __pathHelper(self,visited,q):
        
        while q.empty() is False:
            u = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
                    self.__pathHelper(visited,q)
        
    def path(self):
        visited = [False for i in range(self.nVertices)]
        
        if self.nVertices == 0:
            print("true")
            return 
        
        q = queue.Queue()
        q.put(0)
        visited[0] = True
        self.__pathHelper(visited,q)
        
        if False in visited:
            print("false")
        else:
            print("true")

                
from sys import stdin
import sys
sys.setrecursionlimit(10**8)
a=stdin.readline().strip().split()
n=int(a[0])
m=int(a[1])
g=Graph(n)
li={}
for i in range(m):
    a=stdin.readline().strip().split()
    v1=int(a[0])
    v2=int(a[1])
    g.addedge(v1,v2)

s=g.path()

    
    
Code : All connected components
Send Feedback
Given an undirected graph G(V,E), find and print all the connected components of the given graph G.
Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
3. You need to take input in main and create a function which should return all the connected components. And then print them in the main, not inside function.
Print different components in new line. And each component should be printed in increasing order (separated by space). Order of different components doesn't matter.
Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two space separated integers, that denote that there exists an edge between vertex a and b.
Output Format :
Print different components in new line. And each component should be printed in increasing order of vertices (separated by space). Order of different components doesn't matter.
Constraints :
0 <= V <= 1000
0 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1
Sample Input 1:
4 2
0 1
2 3
Sample Output 1:
0 1 
2 3 
Sample Input 2:
4 3
0 1
1 3 
0 3
Sample Output 2:
0 1 3 
2


# Write your code here

import queue

class Graph:
    
    def __init__(self,n):
        self.nVertices=n
        self.adjMatrix=[[0 for i in range(n)] for j in range(n)]
        
    def addedge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
    def removeedge(self,v1,v2):
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0


    def __pathHelper(self,i,visited,q,li):
        
        q.put(i)
        visited[i] = True
        li.append(i)
        while q.empty() is False:
            u = q.get()
            
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] > 0 and visited[i] is False:
                    self.__pathHelper(i,visited,q,li)
        
        return li
        
    def path(self):
        visited = [False for i in range(self.nVertices)]

        q = queue.Queue()
        l = []
        for i in range(self.nVertices):
            if visited[i] == False:
                l.append(self.__pathHelper(i,visited,q,[]))
        
        if len(l) != 0:
            for i in l:
                print(*i)

                
from sys import stdin
import sys
sys.setrecursionlimit(10**8)
a=stdin.readline().strip().split()
n=int(a[0])
m=int(a[1])
g=Graph(n)
li={}
for i in range(m):
    a=stdin.readline().strip().split()
    v1=int(a[0])
    v2=int(a[1])
    g.addedge(v1,v2)

g.path()

