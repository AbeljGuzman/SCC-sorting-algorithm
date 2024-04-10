import sys 

sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

    def dfs(self, node, visited, stack):
        visited.add(node)
        if node in self.adj_list:
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited, stack)
        stack.append(node)

    def transpose(self):
        transposed_graph = Graph()
        for node in self.adj_list:
            for neighbor in self.adj_list[node]:
                transposed_graph.add_edge(neighbor, node)
        return transposed_graph

    def dfs_scc(self, node, visited, scc):
        visited.add(node)
        scc.append(node)
        if node in self.adj_list:
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    self.dfs_scc(neighbor, visited, scc)

    def find_sccs(self):
        stack = []
        visited = set()

        # First DFS to fill the stack
        for node in self.adj_list:
            if node not in visited:
                self.dfs(node, visited, stack)

        # Transpose the graph
        transposed_graph = self.transpose()

        # Second DFS to find SCCs
        visited.clear()
        largest_scc = []
        while stack:
            node = stack.pop()
            if node not in visited:
                scc = []
                transposed_graph.dfs_scc(node, visited, scc)
                if len(scc) > len(largest_scc):
                    largest_scc = scc

        return largest_scc

# Read the graph from Graph.txt
def read_graph(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        for line in file:
            u, v = map(int, line.strip().split())
            graph.add_edge(u, v)
    return graph

# Write the largest SCC to LSCC.txt
def write_largest_scc(nodes, filename):
    with open(filename, 'w') as file:
        for node in sorted(nodes):
            file.write(str(node) + '\n')

if __name__ == "__main__":
    input_file = "Graph.txt"
    output_file = "LSCC.txt"
    graph = read_graph(input_file)
    largest_scc = graph.find_sccs()
    write_largest_scc(largest_scc, output_file)
