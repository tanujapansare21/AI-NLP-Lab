#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx

graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    k = input("Node: ")
    v = input("Neighbours (comma separated): ").split(',')
    graph[k] = [x for x in v if x]

start = input("Start node: ")

visited = []
queue = [start]

while queue:
    node = queue.pop(0)
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neigh in graph.get(node, []):  
            if neigh not in visited:
                queue.append(neigh)


# -----------------------------------------------
# EXPLANATION OF THE CODE
# -----------------------------------------------

# 1. graph = {}
#    → Creates an empty dictionary to store the graph where
#      keys are node names and values are their connected neighbours.

# 2. n = int(input("Enter number of nodes: "))
#    → Takes the number of nodes in the graph as input from the user.

# 3. for _ in range(n):
#        k = input("Node: ")
#        v = input("Neighbours (comma separated): ").split(',')
#        graph[k] = [x.strip() for x in v if x]
#    → This loop takes each node and its neighbours as input.
#      Example: If Node = A and Neighbours = B,C
#      Then graph becomes {'A': ['B', 'C']}

# 4. start = input("Start node: ")
#    → Asks the user for the starting node to begin BFS traversal.

# 5. visited = []
#    → Creates an empty list to store all visited nodes.

# 6. queue = [start]
#    → Initializes a queue (First-In-First-Out) with the starting node.

# 7. while queue:
#        node = queue.pop(0)
#    → Runs a loop until the queue becomes empty.
#      Removes the first element from the queue (FIFO order).

# 8. if node not in visited:
#        print(node, end=" ")
#        visited.append(node)
#    → Checks if the node is not already visited.
#      If not visited, it prints the node and marks it as visited.

# 9. for neigh in graph.get(node, []):
#        if neigh not in visited:
#            queue.append(neigh)
#    → Finds all neighbours of the current node.
#      If any neighbour is not visited, it is added to the queue
#      so it can be explored later.

# -----------------------------------------------
# OUTPUT EXAMPLE:
# -----------------------------------------------
# Input:
# Enter number of nodes: 4
# Node: A
# Neighbours (comma separated): B,C
# Node: B
# Neighbours (comma separated): D
# Node: C
# Neighbours (comma separated): D
# Node: D
# Neighbours (comma separated):
# Start node: A

# Output:
# A B C D
# -----------------------------------------------
# REAL-TIME USE:
# -----------------------------------------------
# - Used in finding shortest paths in unweighted graphs.
# - Used in social networks to find mutual connections.
# - Used in navigation systems like Google Maps.
# -----------------------------------------------



