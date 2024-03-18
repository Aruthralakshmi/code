class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next =None
class dll:
    def __init__(self):
        self.head=None
    def create(self):
        n = int(input("enter size of list: "))
        for i in range(n):
            data = int(input("enter the array: "))
            self.insertend(data)
    def insertend(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
           temp = temp.next
        temp.next = newnode
        newnode.prev =temp
    def insertatbegining(self):
        data =int(input("enter insert data: "))
        newnode =node(data)        #newnode.next=self.head  #self.head.prev=newnode #self.head = newnode
        newnode.next =self.head
        self.head = newnode
        newnode.next.prev=newnode
    def insertmid(self):
        posi =int(input("enter the position: "))
        data = int(input("enter the number to insertmid: "))
        newnode = node(data)
        temp=self.head
        for i in range(1,posi-1):
            temp=temp.next
        newnode.next = temp.next
        newnode.prev=temp
        temp.next=newnode
        newnode.next.prev=newnode
    def count(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp= temp.next
        print(count)
    def deletefront(self):
        if self.head is not None:
            self.head =self.head.next
            self.head.prev=None
    def deleteend(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next=None
    def deletemid(self):
        posi =int(input("enter the position: "))
        temp=self.head
        for i in range(0,posi-1):
            temp=temp.next
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
    def reverse(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end=" ")
            temp=temp.prev
    def display(self):
        temp = self.head
        while temp.prev:
            print(temp.data,end=" ")
            temp=temp.next
l1= dll()
l1.create()
#l1.insertatbegining()
#l1.insertmid()
#l1.count()
#l1.deletefront()
#l1.deleteend()
#l1.deletemid()
l1.reverse()
#l1.display()
