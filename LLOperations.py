# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
    
    def DeletingFromStart(self,p):
        for _ in range(p):
            if self.head==None:
                break
            self.head=self.head.next
            
    def DisplaySLL(self):
        temp=self.head
        if self.head==None:
            print("List is empty")
            return
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        
    def InsertAtEnd(self,ele):
        node=Node(ele)
        if self.head==None:
            self.head=node
        else:
             temp = self.head
             while temp.next!=None:
                temp = temp.next
             temp.next = node
        
def main():
    N=int(input("Enter the number of elements in the linked list: "))
    arr=list(map(int,input("Enter the elements of the linked list: ").split()))
    p=int(input("Enter the number of elements to delete from the start: "))
    obj=SingleLinkedList()
    for ele in arr:
        h=obj.InsertAtEnd(ele)
    obj.DeletingFromStart(p)
    obj.DisplaySLL()  
main()
