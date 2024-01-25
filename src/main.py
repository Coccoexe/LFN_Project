# Alessio Cocco 2087635, Andrea Valentinuzzi 2090451, Giovanni Brejc 2096046

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

def plotCombinedMetrics(name, degrees, clustering):
    plt.scatter(degrees, clustering, s = 0.1)
    plt.title(name)
    plt.xlabel("Degree Centrality")
    plt.ylabel("Clustering coefficient")
    plt.savefig(OUTPUT_PATH + name + ".png")
    return

def plotHistogram(name, metric, xlabel):
    nbins, mmt = 200, max(metric)
    fig, ax = plt.subplots()
    ax.hist(metric, bins = nbins)
    ax.set(xlim = (0 - 1 / nbins * mmt, mmt + 1 / nbins * mmt)) # ensure 1 bin clearence on both sides for legibility
    plt.title(name)
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
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
    print("START  |  Plotting combined metrics...")
    plotCombinedMetrics(datasets[index][0], dc.scores(), cc.scores())
    print("DONE   |  Metrics PLot saved to file\n")

    # 4. Plot in histogram the distribution of centrality and clustering coefficient separately
    print("START  |  Plotting degree centrality histogram...")
    plotHistogram(datasets[index][0] + "DCHist", dc.scores(), "Degree Centrality")
    print("DONE   |  Degree centrality histogram saved to file\n")
    print("START  |  Plotting clustering coefficient histogram...")
    plotHistogram(datasets[index][0] + "CCHist", cc.scores(), "Clustering Coefficient")
    print("DONE   |  Clustering coefficient histogram saved to file\n")

if __name__ == "__main__":
    main()

