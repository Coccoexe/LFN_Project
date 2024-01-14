import networkx as nx
import matplotlib.pyplot as plt
import os

# Constants

data_path = os.getcwd() + "/data/"

def main():
    print(data_path)
    return

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
