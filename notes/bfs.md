## Breadth First Search (BFS)
- bfs  starts at the [tree root](https://en.wikipedia.org/wiki/Tree_(data_structure)#Terminology "Tree (data structure)") and explores all nodes at the present [depth](https://en.wikipedia.org/wiki/Tree_(data_structure)#Terminology "Tree (data structure)") prior to moving on to the nodes at the next depth level.
- Extra memory is used (usually a queue) to keep track of the child nodes that have not been explored yet. 
- typically best for shortest path algorithms because it searches each node  before moving onto the next
- the example below starts at node A, it also adds each node to a set to avoid revisiting it
- BFS is useful when you need to find the shortest path between any two nodes in an unweighted graph.
- If you're solving a problem, and know a solution is not far from the root of the tree, BFS will likely get you there faster.
```
from collections import deque

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')  # Process the node (in this example, we print it)
        visited.add(node)  # Mark the node as visited
        
        # Enqueue all adjacent nodes that haven't been visited yet
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal:")
bfs(graph, 'A')
```
