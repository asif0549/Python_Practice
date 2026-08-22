from collections import deque
class GraphOperations:
    def __init__(self):
        self.graph={}
    def addEdges(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def displayGraph(self):
        for key,val in self.graph.items():
            print(key,":",val)

    def disconnectedBFS(self,start):
        visited=set()
        visited.add(start)
        self.bfs(start,visited)
        for src in self.graph:
            if src not in visited:
                visited.add(src)
                self.bfs(src,visited)
                
    def bfs(self,start,visited):
        q=deque([start])
        while q:
            curr=q.popleft()
            print(curr,end=" ")
            for N in self.graph[curr]:
                if N not in visited:
                    visited.add(N)
                    q.append(N)

    def DFS(self,start,visited):
        visited.add(start)
        print(start,end=" ")
        for N in self.graph[start]:
            if N not in visited:
                self.DFS(N,visited)

def main():
    nodes=int(input("Enter no.of nodes: "))
    edges=int(input("Enter no.of edges: "))
    obj=GraphOperations()
    for _ in range(edges):
        s,d=input("Enter source and destination: ").split()
        
        obj.addEdges(s,d)
    start=input("Enter start Value: ")
    while True:
        print("\n1. Display graph")
        print("2. Disconnected BFS")
        print("3. DFS")
        print("4. BFS")
        print("5. Exit")
        choice=input("Enter your choice: ")

        match choice:
            case "1":
                obj.displayGraph()
            case "2":
                obj.disconnectedBFS(start)
                print()
            case "3":
                visited=set()
                obj.DFS(start,visited)
                print()
            case "4":
                obj.bfs(start,visited)
                print()
            case "5":
                break
            case _:
                print("Invalid choice")
    
main()
