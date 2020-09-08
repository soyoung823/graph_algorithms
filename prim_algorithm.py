'''
Connect Islands using Prim’s Algorithm
A. Problem Statements
In an ocean, there are n islands some of which are connected via bridges. 
Travelling over a bridge has some cost attaced with it. 
Find bridges in such a way that all islands are connected with minimum cost of travelling.

You can assume that there is at least one possible way in which all islands are connected 
with each other.

You will be provided with two input parameters:

num_islands = number of islands

bridge_config = list of lists. Each inner list will have 3 elements:

 a. island A
 b. island B
 c. cost of bridge connecting both islands
Each island is represented using a number

Example:

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
Input parameters explanation:

1. Number of islands = 4
2. Island 1 and 2 are connected via a bridge with cost = 1
   Island 2 and 3 are connected via a bridge with cost = 4
   Island 1 and 4 are connected via a bridge with cost = 3
   Island 4 and 3 are connected via a bridge with cost = 2
   Island 1 and 3 are connected via a bridge with cost = 10
In this example if we are connecting bridges like this...

between 1 and 2 with cost = 1
between 1 and 4 with cost = 3
between 4 and 3 with cost = 2
...then we connect all 4 islands with cost = 6 which is the minimum traveling cost.

B. Hint: Use a Priority Queue or Min-Heap
In addition to using a graph, you may want to use a custom priority queue for solving this problem. 
If you do not want to create a custom priority queue, you can use Python's inbuilt heapq implementation.

Using the heapq module, you can convert an existing list of items into a min-heap. 
The following two functionalities can be very handy for this problem:

heappush(heap, item) — add item to the heap
heappop(heap) — remove the smallest item from the heap
Let's look at the above methods in action. We start by creating a list of integers.
'''

# heappush
import heapq

# initialize an empty list
minHeap = list()

# insert 5 into heap
heapq.heappush(minHeap, 6)

# insert 6 into heap
heapq.heappush(minHeap, 6)

# insert 2 into heap
heapq.heappush(minHeap, 2)

# insert 1 into heap
heapq.heappush(minHeap, 1)

# insert 9 into haep
heapq.heappush(minHeap, 9)

print('After pushing, heap looks like: {}'.format(minHeap))
# After pushing, heap looks like: [1, 2, 6, 6, 9]

# heappop
# pop and return smallest element from the heap
smallest = heapq.heappop(minHeap)

print('Smallest element in the original list was {}'.format(smallest))
print('After popping, heap looks like: {}'.format(minHeap))

'''
heappush and heappop for items with multiple entries
Note: 
If you insert a tuple inside the heap, the element at 0th index of the tuple is used for comparison.
'''

minHeap = list()
heapq.heappush(minHeap, (0, 1))
heapq.heappush(minHeap, (-1, 5))
heapq.heappush(minHeap, (2, 0))
heapq.heappush(minHeap, (5, -1))
print('After pushing, now heap looks like: {}'.format(minHeap))

# pop and return smallest element from the heap
smallest = heapq.heappop(minHeap)
print('Smallest element in the original list was: {}'.format(smallest))
print('After popping, heap looks like: {}'.format(minHeap))

'''
Now that you know about heapq, you can use it to solve the given problem. 
You are also free to create your own implementatin of Priority Queues.

C. The Idea, based on Prim’s Algorithm:
Our objective is to find the minimum total_cost to visit all the islands. 
We will start with any one island, and follow a Greedy approach.
Step 1 - Create a Graph

Create a graph with given number of islands, and the cost between each pair of islands. 
A graph can be represented as a adjacency_matrix, which is a list of lists. For example, given:
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]

The graph would look like:
graph =  [[], [(2, 1), (4, 3), (3, 10)], [(1, 1), (3, 4)], [(2, 4), (4, 2), (1, 10)], [(1, 3), (3, 2)]]
where, a sublist at  𝑖𝑡ℎ  index represents the adjacency_list of  𝑖𝑡ℎ  island. 
A tuple within a sublist is (neighbor, edge_cost).
Step 2 - Traverse the graph in a Greedy way.
Create a blank minHeap, and push any one island (vertex) into it.
While there are elements remaining in the minHeap, do the following:

Pop out an island having smallest edge_cost, and reduce the heap size. 
You can use heapq.heappop() for this purpose.
If the current island has not been visited before, add the edge_cost to the total_cost. 
You can use a list of booleans to keep track of the visited islands.
Find out all the neighbours of the current island from the given graph. 
Push each neighbour of the current island into the minHeap. 
You can use heapq.heappush() for this purpose.
Mark current island as visited tuple in the adjacency_list of the
When we have popped out all the elements from the minHeap, 
we will have the minimum total_cost to visit all the islands.

D. Exercise - Write the function definition here
Write code in the following function to find and return the minimum cost required 
to travel all islands via bridges.
'''

# The following solution makes use of one of python's priorityQueue implementation (heapq)

def create_graph(num_islands, bridge_config):
    '''
    helper function to create graph using adjacency list implementation
    '''
    graph = [list() for _ in range(num_islands + 1)]
    # populate the adjacency_list
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]

        # an entry in a sublist of graph is represented as a tuple (neighbor, edge_cost)
        graph[source].append((destination, cost))
        graph[destination].append((source, cost))
    
    # try this: print('graph= ', graph)
    return graph

def minimum_cost(graph):
    '''
    helper function to find minimum cost of connecting all islands
    '''

    # start with vertext 1 (any vertex can be chosen)
    start_vertext = 1

    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]

    # heap is represented as a list of tuples
    # a node in heap is represented as tuple (edge_cost, neighbor)
    minHeap = [(0, start_vertext)]
    total_cost = 0

    while len(minHeap) > 0:
        # here, heapq.heappop() will automatically pop out the node having smallest edge_cost, 
        # and reduce the heap size
        cost, current_vertext = heapq.heappop(minHeap)

        # check if current_vertex is already visited
        if visited[current_vertext]:
            continue

        # else add cost to total_cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertext]:
            heapq.heappush(minHeap, (edge_cost, neighbor))
        
        # mark current_vertest as visited
        visited[current_vertext] = True

    return total_cost


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all islands
    """
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)

def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
