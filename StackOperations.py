class StackOperations:
    def __init__(self, c):
        self.stack = []
        self.capacity = c

    def push(self, val):
        if len(self.stack) == self.capacity:
            print("="*20)
            print("Stack OverFlow")
            print("="*20)
        else:
            self.stack.append(val)
            print(f"Pushed {val} into stack")

    def pop(self):
        if self.isEmpty():
            print("="*20)
            print("Stack Underflow")
            print("="*20)
        else:
            print("Popped:", self.stack.pop())

    def peek(self):
        if self.isEmpty():
            print("="*20)
            print("Stack Underflow")
            print("="*20)
        else:
            print("Top of the stack is:", self.stack[-1])

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity

    def Display(self):
        print("Stack:", self.stack)


def main():
    print("Stack Operations")
    c = int(input("Enter the capacity: "))
    obj = StackOperations(c)

    while True:
        print("\n1.Push")
        print("2.Pop")
        print("3.Peek")
        print("4.isEmpty")
        print("5.isFull")
        print("6.Display")
        print("7.Exit")

        op = int(input("Enter option: "))

        match op:
            case 1:
                val = int(input("Enter value to push: "))
                obj.push(val)

            case 2:
                obj.pop()

            case 3:
                obj.peek()

            case 4:
                print("Stack is Empty" if obj.isEmpty() else "Stack is Not Empty")

            case 5:
                print("Stack is Full" if obj.isFull() else "Stack is Not Full")

            case 6:
                obj.Display()

            case 7:
                print("============ End ===========")
                break

            case _:
                print("Invalid Option")
                break


main()