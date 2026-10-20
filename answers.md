The graph is stored using an adjacency list implementation. I chose a standard Python dictionary (self.adj_list) where each key is a node integer and the value is a list of connected neighboring nodes.
I chose an adjacency list rather than an adjacency matrix because adjacency lists are significantly more memory-efficient and faster for sparse graphs (such as g7.txt with 1,000,000 nodes but only 2,967,232 edges), taking O(m+n) space. 
To manage the graph, the structure also stores num_nodes and num_edges as basic integer fields to validate graph size For the third algorithm, I selected Iterative Deepening Depth-First Search (IDDFS). 
I chose this because it elegantly bridges the gap between BFS and DFS. 
It utilizes the space efficiency of DFS (O(d) where d is the maximum depth) but explores level-by-level, guaranteeing the shortest path in unweighted graphs like BFS Both BFS and DFS store a Python set of visited nodes. 
This allows O(1) constant-time lookup to determine if a node has already been processed, preventing infinite loops in cyclic graphs BFS uses a deque (double-ended queue) to manage the frontier, ensuring O(1) pop operations from the front. 
DFS uses a standard list as a stack, providing O(1) push and pop operations from the end Both algorithms maintain a search_tree list containing tuples of (parent, child) edges to track the path taken. 
DFS also utilizes a parent_map dictionary during traversal to map correctly which node pushed the current neighbor onto the stack
The choice of starting node generally does not make a mathematically significant order-of-magnitude difference in the overall run time for standard unweighted graphs.
The algorithm still must traverse all connected nodes and edges O(m+n) within the component regardless of where it begins is this fine for a readme 
