import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3,4,5,6,7,8,9,10])

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,5)
G.add_edge(5,9)
G.add_edge(3,6)
G.add_edge(3,7)
G.add_edge(7,10)
G.add_edge(4,8)

bfs_output=list(nx.bfs_tree(G,source=1))

print(bfs_output)

nx.draw(G,with_labels=True,node_color="magenta",font_weight="bold")
plt.show()

