from collections import deque
class Node:
    def __init__(self,d):
        self.left=None
        self.data=d
        self.right=None
class BTOperations:
    def __init__(self):
        self.root=None
        
    def CreateBT(self,arr):
        if len(arr)==0:
            return 
        self.root=Node(arr[0])
        q=deque()
        q.append(self.root)
        idx=1
        while len(q)!=0 and idx < len(arr):
            curr=q.popleft()
            if idx < len(arr):
                curr.left=Node(arr[idx])
                q.append(curr.left)
            idx +=1

            if idx < len(arr):
                curr.right=Node(arr[idx])
                q.append(curr.right)
            idx +=1
        return self.root

    def Inorder(self,node):
        if node==None:
            return
        self.Inorder(node.left)
        print(node.data,end=" ")
        self.Inorder(node.right)

    def replace(self,root,old,new):
        if root==None:
            return 
        q=deque([root])
        flag=True
        while q:
            curr=q.popleft()
            if curr.data==old:
                curr.data=new
                flag=False
                return
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
        if flag:
            print("Element Not found to replace")

    def AddNode(self,root,new):
        if self.root==None:
            self.root=new
            return
        q=deque([root])
        while q:
            curr=q.popleft()
            if curr.left==None :#or curr.left=='null':
                curr.left=Node(new)
                return self.root
            else:
                q.append(curr.left)

            if curr.right==None: # or curr.right=='null':
                curr.right=Node(new)
                return self.root
            else:
                q.append(curr.right)
        return self.root
    def RemovingNode(self,root,val):
        if self.root==None:
            print("No Nodes to Delete from Binary Tree.")
            return 

        q=deque([(root,None)])
        target=None
        target_parent=None
        last_node=None
        last_parent=None

        while q:
            curr,parent = q.popleft()
            last_node=curr
            last_parent=parent

            if curr.data==val:
                target=curr
                target_parent=parent

            if curr.left!=None:
                q.append((curr.left,curr))
            if curr.right!=None:
                q.append((curr.right,curr))

        if target==None:
            print("Element not found")
            return

        if target is last_node:
            if target_parent==None:
                self.root=None
            elif target_parent.left is target:
                target_parent.left=None
            else:
                target_parent.right=None
            return

        target.data=last_node.data

        if last_parent!=None:
            if last_parent.left is last_node:
                last_parent.left=None
            else:
                last_parent.right=None

    
def main():
    arr=[5,4,10,3,8]
    obj=BTOperations()
    r=obj.CreateBT(arr)
    option=int(input("Enter options: \n1.Inorder Traversal \n2.Replace node data \n3.Adding a Node \n4.Deleting a Node \n"))
    match(option):
        case 1:
            print("Inorder")
            obj.Inorder(r)
        case 2:
            print("\nUpdated Tree")
            obj.replace(r,4,50)
            obj.Inorder(r)
        case 3:
            print("After Adding Node")
            obj.AddNode(r,49)
            obj.Inorder(r)
        case 4:
            print("after Deleting Node:")
            obj.RemovingNode(r,4)
            obj.Inorder(r)
main()