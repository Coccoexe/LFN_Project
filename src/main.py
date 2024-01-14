# Alessio Cocco 2087635, Andrea Valentinuzzi 2090451, Giovanni Brejc xxxxxxx

import networkx as nx
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

# Constants

data_path = os.getcwd() + "/data/"

def compute_centrality(graph: nx.Graph):
    # Computes degree centrality of each node
    return nx.degree_centrality(graph)

def compute_clustering_coefficient(graph: nx.Graph):
    for node in tqdm(graph.nodes()):
        graph.nodes[node]['clustering_coefficient'] = nx.clustering(graph, node)
    return

def plot_centrality_clustering():
    return

def main():
    # Dataset selection
    datasets = [[file.replace('.edges', ''), data_path + file] for file in os.listdir(data_path) if file.endswith(".edges")]    
    print("Choose a dataset:")
    for i, dataset in enumerate(datasets):
        print(i, dataset[0])
    index = int(input())

    # Networkx graph object
    print("\nSTART  |  Reading graph\'", datasets[index][0], "\'...")
    graph = nx.read_weighted_edgelist(datasets[index][1])
    print("DONE   |  Graph read\n")

    # 1. Compute degree centrality of each node
    #compute_centrality(graph)

    # 2. Compute clustering coefficient of each node
    compute_clustering_coefficient(graph)

    # 3. Plot in scatter plot centrality (x) and clustering coefficient (y)

    

if __name__ == "__main__":
    main()

exit()

# read the graph from a weighted edges file and create a networkx graph object
fh = open("C:/Users/giovanni/Desktop/lfn/bio-human-gene1.edges", "rb")
G = nx.read_weighted_edgelist(fh)
print("hello")
fh.close()
#compute the degree of each node and print the maximum degree and the average degree of the graph G 
degree_sequence = sorted([d for n, d in G.degree()], reverse = True)
dmax = max(degree_sequence)
davg = np.mean(degree_sequence)
print("Maximum degree", dmax)
print("Average degree", davg)
#print graph info
print(nx.info(G))


d = nx.degree_centrality(G)
print("hello2")

d = nx.betweenness_centrality(G)
#print d in a file with the following format: node_id betweenness_centrality
f = open("C:/Users/giovanni/Desktop/lfn/betweenness_centrality.txt", "w")
for key, value in d.items():
    f.write("%s %s\n" % (key, value))
f.close()
print("hello4")



#compute betweenness centrality of each node and print the maximum betweenness centrality and the average betweenness centrality of the graph G
#betweenness_sequence = sorted([b for n, b in nx.betweenness_centrality(G).items()], reverse=True)
#bmax = max(betweenness_sequence)
#bavg = np.mean(betweenness_sequence)
#print("Maximum betweenness centrality", bmax)
#print("Average betweenness centrality", bavg)
#compute closeness centrality of each node and print the maximum closeness centrality and the average closeness centrality of the graph G
#closeness_sequence = sorted([c for n, c in nx.closeness_centrality(G).items()], reverse=True)
#cmax = max(closeness_sequence)
#cavg = np.mean(closeness_sequence)
#print("Maximum closeness centrality", cmax)
#print("Average closeness centrality", cavg)
