def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbour in graph.get(start, []):
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

def bfs(graph, start):
    visited = set([start])
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")
        for neighbour in graph.get(vertex, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


class BSTNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self.insert_node(self.root, key)

    def insert_node(self, current, key):
        if key < current.val:
            if current.left is None:
                current.left = BSTNode(key)
            else:
                self.insert_node(current.left, key)
        elif key > current.val:
            if current.right is None:
                current.right = BSTNode(key)
            else:
                self.insert_node(current.right, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")

    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def create_graph():
    graph = {}
    n = int(input("Enter number of vertices: "))
    print("Enter vertex followed by its neighbors (e.g., A B C):")
    
    for i in range(n):
        parts = input().split()
        vertex = parts[0]
        neighbors = parts[1:]
        graph[vertex] = neighbors
        
    return graph

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E'] 
# }

graph = create_graph()
print("Depth First Search")
dfs(graph, 'A')
print("\n")

print("Breadth First Search (BFS)")
bfs(graph, 'A')
print("\n")

print("Binary Search Tree (BST) Traversals")

'''Tree Structure:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80'''


bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print("Inorder Traversal (Sorted):")
bst.inorder(bst.root)

print("\nPreorder Traversal:")
bst.preorder(bst.root)

print("\nPostorder Traversal:")
bst.postorder(bst.root)

print("\nLevel Order Traversal:")
bst.level_order()
print()