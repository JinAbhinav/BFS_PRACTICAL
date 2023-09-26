import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (5, 6)])

# Perform BFS
def breadth_first_search(graph, start_node):
    visited = set()
    queue = [start_node]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            neighbors = list(graph.neighbors(node))
            queue.extend(neighbors)
    return visited

# Visualize the graph and BFS traversal
def visualize_graph_and_bfs(graph, bfs_result):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='lightblue')
    
    labels = {node: node if node in bfs_result else '' for node in graph.nodes()}
    nx.draw_networkx_labels(graph, pos, labels, font_size=12)
    
    plt.title("Breadth-First Search Visualization")
    plt.show()

start_node = 1  # Starting node for BFS
bfs_result = breadth_first_search(G, start_node)
visualize_graph_and_bfs(G, bfs_result)