import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()
G.add_edge(0,1,weight=1)
G.add_edge(0,2,weight=3)
G.add_edge(1,3,weight=5)
G.add_edge(2,3,weight=1)
G.add_edge(2,4,weight=2)
G.add_edge(3,4,weight=1)
G.add_edge(3,5,weight=2)
G.add_edge(4,5,weight=4)

shortest=nx.shortest_path(G,source=0,target=5,weight='weight')

shortestL=nx.shortest_path_length(G,source=0,target=5,weight='weight')

print(shortestL)

pos=nx.spring_layout(G)
nx.draw(G,with_labels=True,node_color="orange",edge_color='red',arrows=True)
plt.show()
