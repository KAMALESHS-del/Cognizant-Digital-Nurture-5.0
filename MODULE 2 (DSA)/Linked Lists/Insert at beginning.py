class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(20)
n3=node(30)
n1.next=n2
n2.next=n3
head=n1
"insert at begining"
n4=node(300)
n4.next=head
head=n4
while head:
    print(head.data,end="->")
    head=head.next
print("NONE")



