class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node
    
    def insert_after(self, node, value):
        new_node = Node(value)
        next_node = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = next_node
        if next_node:
            next_node.prev = new_node
        else:
            self.tail = new_node
        return new_node
    
    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

queries = int(input())

array = DoublyLinkedList()
hash_map = {}

for _ in range(queries):
    query = list(input().split(" "))
    
    if query[0] == 'insert':
        x, y = int(query[1]), int(query[2])  
        
        if y in hash_map:
            node_y = hash_map[y]
            new_node = array.insert_after(node_y, x)
        else:
            new_node = array.append(x)
        
        if x not in hash_map:
            hash_map[x] = new_node  
    
    elif query[0] == 'remove':
        x = int(query[1])  

        if x in hash_map:
            node_x = hash_map[x]
            array.remove(node_x)
            del hash_map[x]

result = []
current = array.head
while current:
    result.append(current.value)
    current = current.next

print(" ".join(map(str, result)))
