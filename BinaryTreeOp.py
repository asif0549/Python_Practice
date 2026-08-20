from collections import deque
class Node:
    def __init__(self,d):
        self.left=None
        self.data=d
        self.right=None
class BTOperations:
    def __init__(self):
        self.root=None

    def createBT(self,arr):
        if len(arr)==0:
            return 
        self.root=Node(arr[0])
        q=deque()
        q.append(self.root)
        idx=1

        while len(q)!=0 and idx < len(arr):
            curr=q.popleft()
            if idx < len(arr) and arr[idx]!="null":
                curr.left=Node(arr[idx])
                q.append(curr.left)
            idx +=1

            if idx < len(arr) and arr[idx]!="null":
                curr.right=Node(arr[idx])
                q.append(curr.right)
            idx +=1

        return self.root
#==================================================BFS======================================================
    def levelOrder(self,root):
        if root==None:
            return 
        q=deque()
        q.append(root)
        while len(q)!=0:
            curr=q.popleft()
            print(curr.data,end=" ")
            
            if curr.left!=None:
                q.append(curr.left)
                
            if curr.right!=None:
                q.append(curr.right)
#=================================================DFS=======================================================
    def PreOrder(self,root):
        if root==None:
            return
        print(root.data,end=" ")
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def InOrder(self,root):
        if root==None:
            return
        self.InOrder(root.left)
        print(root.data,end=" ")
        self.InOrder(root.right)

    def PostOrder(self,root):
        if root==None:
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.data,end=" ")
#==============================================================================================================
            
def main():
    arr=list(map(int,input("Enter the elements of the binary tree in level order : \n").strip().split()))
    obj=BTOperations()
    Root=obj.createBT(arr)
    obj.levelOrder(Root)
    print("\nPre Order:")
    obj.PreOrder(Root)
    print("\nInOrder: ")
    obj.InOrder(Root)
    print("\nPostOrder")
    obj.PostOrder(Root)
main()
    