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

def plotMetrics(name, degrees, clustering):
    plt.scatter(degrees, clustering)
    plt.title(name)
    plt.xlabel("Degree Centrality")
    plt.ylabel("Clustering coefficient")
    plt.savefig(OUTPUT_PATH + name + ".png")
    return

def saveToFile(filename, data):
    with open(OUTPUT_PATH + filename + '.txt', "w+") as f:
        for i in range(len(data)):
            f.write(str(i) + " " + str(data[i]) + "\n")

def main():

    if not os.path.exists(DATA_PATH):
        print("ERROR  |  Data folder not found. Please create a folder named 'data' and put the datasets inside it.")
        return

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
    graph = nk.readGraph(datasets[index][1], nk.Format.EdgeList, separator=' ', firstNode=0, continuous=False)
    print("DONE   |  Graph read!\n")

    # 1. Compute degree centrality of each node
    print("START  |  Computing degree centrality...")
    dc = degreeCentrality(graph)
    saveToFile(datasets[index][0] + "_degree_centrality", dc.scores())
    print("DONE   |  Degree centrality computed\n")

    # 2. Compute clustering coefficient of each node
    print("START  |  Computing clustering coefficient...")
    cc = clusteringCoefficient(graph)
    saveToFile(datasets[index][0] + "_clustering_coefficient", cc.scores())
    print("DONE   |  Clustering coefficient computed\n")

    # 3. Plot in scatter plot centrality (x) and clustering coefficient (y)
    print("START  |  Plotting metrics...")
    plotMetrics(datasets[index][0], dc.scores(), cc.scores())
    print("DONE   |  Metrics PLot saved to file\n")

if __name__ == "__main__":
    main()