class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(30)
n2 = Node(40)
n3 = Node(60)
n4=Node(100)

n1.next = n2
n2.next = n3
n3.next=n4

head = n1

count = 0

while head:
    count += 1
    head = head.next

print("Total Nodes:", count)