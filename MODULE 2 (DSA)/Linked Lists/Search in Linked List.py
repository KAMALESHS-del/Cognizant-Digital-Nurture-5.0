"Find whether a value exists in the linked list."
class node():
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(30)
n2=node(40)
n3=node(60)
n1.next=n2
n2.next=n3
tar=50
head=n1
while head:
    if head.data==tar:
        print("element found")
        break
    head=head.next
else:
    print("not found")
        