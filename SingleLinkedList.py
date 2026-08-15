class Node:
    def __init__(self,d):
        self.data=d
        self.next=None

class LinkedlistOperations:
    def __init__(self):
        self.head=None

    def addNodeAtEnd(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=node
        return self.head

    def AddNodeAtBeg(self,val):
        node=Node(val)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
        return self.head

    def InsertNodeAtPosition(self,p,value):
        node=Node(value)
        temp=self.head
        if p==1:
            node.next=self.head
            self.head=node
            return
            
        else:
            for _ in range(p-2):
                temp=temp.next
            node.next=temp.next
            temp.next=node
        return self.head 
                  

    def DeletingAtPosition(self,p):
        temp=self.head
        if p==1:
            self.head=self.head.next
            return self.head
        else:
            for _ in range(p-2):
                temp=temp.next
            temp.next=temp.next.next
        return self.head
                
                
    def DisplayLinkedList(self,head):
        temp=head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        
        

def main():
    arr=[10,20,30]
    obj=LinkedlistOperations()
    for  ele in arr:
        obj.addNodeAtEnd(ele)
    print("Linked List Operations:\n1.Adding node at end \n2.Adding Node at beginning \n3.Inserting node at particular position \n4.Deleting node at particular position")
    op=int(input("Please select a option(1-4):"))
    match(op):
        case 1:
                e=int(input("Enter element to insert at end: "))
                y=obj.addNodeAtEnd(e)
                obj.DisplayLinkedList(y)
                
        case 2:
            r=int(input("Enter integer to add at beginning: "))
            x=obj.AddNodeAtBeg(r)
            obj.DisplayLinkedList(x)
        case 3:
            a=int(input("Enter Position: "))
            b=int(input("Enter element to insert: "))
            h=obj.InsertNodeAtPosition(a,b)
            obj.DisplayLinkedList(h)
        case 4:
            d=int(input("Enter position to delete element: "))
            a=obj.DeletingAtPosition(d)
            obj.DisplayLinkedList(a)
        case _:
            print("Invalid Operand")
            return
        
main()