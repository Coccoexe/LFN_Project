# Alessio Cocco 2087635, Andrea Valentinuzzi 2090451, Giovanni Brejc xxxxxxx

import networkit as nk
import matplotlib.pyplot as plt
import os
    
# Constants
DATA_PATH = os.getcwd() + "/data/"
OUTPUT_PATH = os.getcwd() + "/output/"

def degreeCentrality(graph):
    return nk.centrality.DegreeCentrality(graph).run()

def clusteringCoefficient(graph):
    graph.removeSelfLoops()
    return nk.centrality.LocalClusteringCoefficient(graph).run()

def plotMetrics():
    return

def saveToFile(filename, data):
    with open(OUTPUT_PATH + filename + '.txt', "w+") as f:
        for i in range(len(data)):
            f.write(str(i) + " " + str(data[i]) + "\n")

def main():
    # Dataset selection
    datasets = [[file.replace('.edges', ''), DATA_PATH + file] for file in os.listdir(DATA_PATH) if file.endswith(".edges")]    
    print("Choose a dataset:")
    for i, dataset in enumerate(datasets):
        print(i, dataset[0])
    index = int(input())

    # Create output folder
    if not os.path.exists("./output"): os.makedirs("./output")

    # Setup graph
    print("START  |  Reading graph", datasets[index][0], "...")
    graph = nk.readGraph(datasets[index][1], nk.Format.EdgeList, separator = ' ', firstNode = 0, continuous = False)
    print("DONE   |  Graph read!\n")

    # 1. Compute degree centrality of each node
    print("START  |  Computing degree centrality...")
    dc = degreeCentrality(graph)
    saveToFile("degree_centrality", dc.scores())
    print("DONE   |  Degree centrality computed\n")

    # 2. Compute clustering coefficient of each node
    print("START  |  Computing clustering coefficient...")
    cc = clusteringCoefficient(graph)
    saveToFile("clustering_coefficient", cc.scores())
    print("DONE   |  Clustering coefficient computed\n")

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
