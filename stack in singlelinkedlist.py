class node:
    def _init_(self,data):
        self.data=data
        self.next=None
class stack_sll:
    def _init_(self):
        self.top=None
    def push(self,data):
        newnode=node(data)
        if self.top==None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.top==None:
            print("Underflow")
        else:
            print(self.top.data)
            self.top=self.top.next
    def peek(self):
        print(self.top.data)
    def display(self):
        temp=self.top
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
l1=stack_sll()
n=int(input("enter no:"))
for i in range(0,n):
    data=int(input("enter data:"))
    l1.push(data)
l1.pop()
#l1.peek()
l1.display()
