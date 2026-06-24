"Delete a Node in Linked List"
"""There are 3 deletion cases:

Delete first node (head) → head = head.next
Delete middle node → curr.next = curr.next.next
Delete last node → find previous node and set:
curr.next = None

These are the standard linked-list deletion patterns."""

"Delete first node (head) → head = head.next"
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

head = n1

head = head.next
curr=head
while curr:
    print(curr.data)
    curr=curr.next


"Delete last node → find previous node and set"

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1

curr = head

while curr.next.next:
    curr = curr.next

curr.next = None

# Traverse
curr = head

while curr:
    print(curr.data, end=" -> ")
    curr = curr.next

print("None")


"Delete middle node → curr.next = curr.next.next"
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3
tar=20

head = n1
curr=head
while curr.next:
    if curr.next.data==tar:
        curr.next=curr.next.next
        break
    curr=curr.next

curr=head
while curr:
    print(curr.data)
    curr=curr.next
print("NONE")    