class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

head = n1

# New node
new_node = Node(40)

curr = head

while curr.next:
    curr = curr.next

curr.next = new_node




while head:
    print(head.data, end=" -> ")
    head = head.next

print("None")