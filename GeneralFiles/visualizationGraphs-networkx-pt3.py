#Reference: https://www.geeksforgeeks.org/directed-graphs-multigraphs-and-visualization-in-networkx/
#Description: Generates a DiGraph representation and plot it with matplotlib.

import networkx as nx 
import matplotlib.pyplot as plt 

G = nx.DiGraph()
G.add_edges_from([(1, 1), (1, 7), (2, 1), (2, 2), (2, 3),  
                  (2, 6), (3, 5), (4, 3), (5, 4), (5, 8), 
                  (5, 9), (6, 4), (7, 2), (7, 6), (8, 7)]) 
  
plt.figure(figsize =(6, 6)) 
nx.draw_networkx(G, with_labels = True, node_color ='green') 
  
# getting different graph attributes 
print("Total number of nodes: ", int(G.number_of_nodes())) 
print("Total number of edges: ", int(G.number_of_edges())) 
print("List of all nodes: ", list(G.nodes())) 
print("List of all edges: ", list(G.edges())) 
print("In-degree for all nodes: ", dict(G.in_degree())) 
print("Out degree for all nodes: ", dict(G.out_degree)) 
print("List of all nodes we can go to in a single step from node 2: ", list(G.successors(2)))   
print("List of all nodes from which we can go to node 2 in a single step: ", list(G.predecessors(2))) 

plt.show()