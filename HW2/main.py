import time
import sys
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.num_nodes = 0
        self.num_edges = 0

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.read().split()
            if not lines:
                return
            
            self.num_nodes = int(lines[0])
            self.adj_list = {i: [] for i in range(self.num_nodes)}
            
            edges = lines[1:]
            self.num_edges = len(edges) // 2
            
            for i in range(0, len(edges), 2):
                u = int(edges[i])
                v = int(edges[i+1])
                self.adj_list[u].append(v)
                self.adj_list[v].append(u) # Assuming undirected graph based on typical edge lists

def bfs(graph, start_node):
    visited = {start_node}
    queue = deque([start_node])
    search_tree = []
    
    while queue:
        current = queue.popleft()
        for neighbor in graph.adj_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                search_tree.append((current, neighbor))
                queue.append(neighbor)
    return search_tree

def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    search_tree = []
    parent_map = {start_node: None}
    
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            if parent_map[current] is not None:
                search_tree.append((parent_map[current], current))
            
            # Sort reversed to visit in numerical order for predictable results
            for neighbor in sorted(graph.adj_list[current], reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)
                    parent_map[neighbor] = current
    return search_tree

def iddfs(graph, start_node, max_depth=1000):
    def dls(node, depth, visited, search_tree):
        if depth == 0:
            return True
        if depth > 0:
            for neighbor in graph.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    search_tree.append((node, neighbor))
                    dls(neighbor, depth - 1, visited, search_tree)
                    # Note: strict tree building in IDDFS involves complex path tracking.
                    # This simplified version checks reachability within depth limits.
        return False

    search_tree = []
    for depth in range(max_depth):
        visited = {start_node}
        current_tree = []
        dls(start_node, depth, visited, current_tree)
        if len(visited) == graph.num_nodes:
            return current_tree
    return search_tree

def measure_time(algorithm, graph, start_node, iterations=5):
    times = []
    search_tree = None
    for _ in range(iterations):
        start_time = time.perf_counter()
        search_tree = algorithm(graph, start_node)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    
    avg_time = sum(times) / len(times)
    return avg_time, search_tree

def save_tree(filename, tree):
    with open(filename, 'w') as f:
        for u, v in tree:
            f.write(f"{u} -> {v}\n")

def main():
    filename = input("Enter the input graph file name: ")
    g = Graph()
    try:
        g.load_from_file(filename)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
        
    print(f"Graph loaded. Nodes (n): {g.num_nodes}, Edges (m): {g.num_edges}")
    
    try:
        start_node = int(input(f"Enter starting node (0 to {g.num_nodes - 1}): "))
    except ValueError:
        print("Invalid node.")
        sys.exit(1)

    algorithms = {
        "BFS": bfs,
        "DFS": dfs,
        "IDDFS": iddfs
    }

    print("\nRunning searches...")
    for name, algo in algorithms.items():
        avg_time, tree = measure_time(algo, g, start_node, iterations=5)
        print(f"{name} Average Time (5 runs): {avg_time:.6f} seconds")
        
        out_file = f"{name}_tree_{filename}"
        save_tree(out_file, tree)
        print(f"  -> Search tree saved to {out_file}")

if __name__ == "__main__":
    main()
