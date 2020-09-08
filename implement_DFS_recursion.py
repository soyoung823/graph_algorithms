'''
Graph Depth-First Search With Recursion
We've done depth-first search previously using an iterative approach (i.e., using a loop). 
In this notebook, we'll show how to implement a recursive soluton.

The basic idea is to select a node and explore all the possible paths from that node, 
and to apply this recursively to each node we are exploring.

You can see some helpful illustrations with various combinations here: 
https://www.cs.usfca.edu/~galles/visualization/DFS.html
'''

# For this exercise we will be using an Adjacency List representation to store the graph.

# class Node representation.
class Node:
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph:
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        node1.add_child(node2)
        node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes) and (node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)

# creating a graph
nodeG = Node('G')
nodeR = Node('R')
nodeA = Node('A')
nodeP = Node('P')
nodeH = Node('H')
nodeS = Node('S')

graph1 = Graph([nodeG, nodeR, nodeA, nodeP, nodeH, nodeS])

graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeR, nodeA)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeG, nodeH)
graph1.add_edge(nodeR, nodeS)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeP, nodeH)

# To verify that the  graph is created accurately.
# Let's just print all the parent nodes and child nodes.
for each in graph1.nodes:
    print('parent node = ', each.value, end='\nchildren\n')
    for each in each.children:
        print(each.value, end=' ')
    print('\n')

'''
parent node =  G
children
R A H 

parent node =  R
children
G A S P 

parent node =  A
children
R G 

parent node =  P
children
R H 

parent node =  H
children
G P 

parent node =  S
children
R 
'''

'''
Sample input and output
The output would vary based on the implementation of your algorithm, 
the order in which children are stored within the adjacency list.

DFS using recursion
Now that we have our example graph initialized, we are ready to do the actual depth-first search. 
Here's what that looks like:
'''

'''TODO'''
def dfs_recursion_start(start_node, search_value):
    visited = set() # set to keep track of visited nodes.
    return dfs_recursion(start_node, visited, search_value)

# recursive function
def dfs_recursion(node, visited, search_value):
    if node.value == search_value:
        found = True    # don't search in other branches, if found = True
        return node
    
    visited.add(node)
    found = False
    result = None

    # conditional recurses on each neighbour.
    for child in node.children:
        if child not in visited:
            result = dfs_recursion(child, visited, search_value)

            # once the match is found, no more recurses
            if found:
                break
    return result

    assert nodeA == dfs_recursion_start(nodeG, 'A')
    assert nodeA == dfs_recursion_start(nodeS, 'A')
    assert nodeS == dfs_recursion_start(nodeP, 'S')
    assert nodeR == dfs_recursion_start(nodeH, 'R')
