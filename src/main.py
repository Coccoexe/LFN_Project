# Alessio Cocco 2087635, Andrea Valentinuzzi 2090451, Giovanni Brejc 2096046
#
# Code subdivision
#   Alessio  -  degree-cc-scatter
#   Andrea   -  eigen-betweenness-histograms
#   Giovanni -  traingles-radars
#   
#   The structure of the main was planned at the beginning of the project,
#   each member following the structure has written the code correlated to his part.

import networkit as nk
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# Constants
DATA_PATH = os.getcwd() + "/data/"
OUTPUT_PATH = os.getcwd() + "/output/"
skip = True
dataset = None

def degreeCentrality(graph):
    if skip and os.path.exists(OUTPUT_PATH + dataset[0] + "_degree_centrality.txt"):
        return loadFromFile(dataset[0] + "_degree_centrality")
    return nk.centrality.DegreeCentrality(graph).run()

def clusteringCoefficient(graph):
    if skip and os.path.exists(OUTPUT_PATH + dataset[0] + "_clustering_coefficient.txt"):
        return loadFromFile(dataset[0] + "_clustering_coefficient")
    graph.removeSelfLoops()
    return nk.centrality.LocalClusteringCoefficient(graph).run()

def betweennessCentrality(graph):
    if skip and os.path.exists(OUTPUT_PATH + dataset[0] + "_betweenness_centrality.txt"):
        return loadFromFile(dataset[0] + "_betweenness_centrality")
    return nk.centrality.Betweenness(graph).run()

def eigenCentrality(graph):
    if skip and os.path.exists(OUTPUT_PATH + dataset[0] + "_eigen_centrality.txt"):
        return loadFromFile(dataset[0] + "_eigen_centrality")
    return nk.centrality.EigenvectorCentrality(graph).run()

def countTriangles(graph):
    if skip and os.path.exists(OUTPUT_PATH + dataset[0] + "_triangles.txt"):
        return loadFromFile(dataset[0] + "_triangles")
    if type(graph) is not nx.Graph:
        graph = nk.nxadapter.nk2nx(graph)
    return nx.triangles(graph)

def plotRadarChart(name, metrics):
    
    # normalize
    for i in range(len(metrics)):
        max_, min_ = max(metrics[i]), min(metrics[i])
        for j in range(len(metrics[i])):
            metrics[i][j] = (metrics[i][j] - min_) / (max_ - min_)

    # compute mean
    data = [0] * len(metrics)
    for i in range(len(metrics)):
        data[i] = sum(metrics[i]) / len(metrics[i])

    # plot
    labels = ['Degree Centrality', 'Clustering Coefficient', 'Eigen Centrality', 'Betweenness Centrality', 'Triangles']
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, data, 'o-', linewidth=2)
    ax.fill(angles, data, alpha=0.25)
    ax.set_thetagrids(angles * 180 / np.pi, labels)
    ax.set_title(name)
    ax.grid(True)
    plt.savefig(OUTPUT_PATH + name + ".png")
    return

def plotCombinedMetrics(name, degrees, clustering):
    fig , ax = plt.subplots()
    ax.scatter(degrees, clustering, s = 0.1)
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

def loadFromFile(filename):
    data = []
    with open(OUTPUT_PATH + filename + '.txt', "r") as f:
        for line in f:
            data.append(float(line.split()[1]))
    return data

def main():
    global skip
    global dataset
    
    #  ___       _ _   _       _ _          _   _             
    # |_ _|_ __ (_) |_(_) __ _| (_)______ _| |_(_) ___  _ __  
    #  | || '_ \| | __| |/ _` | | |_  / _` | __| |/ _ \| '_ \ 
    #  | || | | | | |_| | (_| | | |/ / (_| | |_| | (_) | | | |
    # |___|_| |_|_|\__|_|\__,_|_|_/___\__,_|\__|_|\___/|_| |_|
                                                           
    if not os.path.exists(DATA_PATH):
        print("ERROR  |  Data folder not found. Please create a folder named 'data' and put the datasets inside it.")
        return

    # Dataset selection
    datasets = [[file.replace('.edges', ''), DATA_PATH + file] for file in os.listdir(DATA_PATH) if file.endswith(".edges")]    
    print("Choose a dataset:")
    for i, dataset in enumerate(datasets):
        print(i, dataset[0])
    index = int(input())
    dataset = datasets[index]

    print("\nWant to force recomputation of metrics? (y/N)")
    input_ = input()
    if input_ == 'y' or input_ == 'Y': skip = False

    # Create output folder
    if not os.path.exists("./output"): os.makedirs("./output")

    # Setup graph
    print("START  |  Reading graph", datasets[index][0], "...")
    graph = nk.readGraph(datasets[index][1], nk.Format.EdgeList, separator = ' ', firstNode = 0, continuous = False)
    print("DONE   |  Graph read!\n")

    #                 _        _          
    #  _ __ ___   ___| |_ _ __(_) ___ ___ 
    # | '_ ` _ \ / _ \ __| '__| |/ __/ __|
    # | | | | | |  __/ |_| |  | | (__\__ \
    # |_| |_| |_|\___|\__|_|  |_|\___|___/

    # degree centrality
    print("START  |  Computing degree centrality...")
    dc = degreeCentrality(graph)
    if type(dc) is not list: dc = dc.scores()
    saveToFile(datasets[index][0] + "_degree_centrality", dc)
    print("DONE   |  Degree centrality computed\n")

    # clustering coefficient
    print("START  |  Computing clustering coefficient...")
    cc = clusteringCoefficient(graph)
    if type(cc) is not list: cc = cc.scores()
    saveToFile(datasets[index][0] + "_clustering_coefficient", cc)
    print("DONE   |  Clustering coefficient computed\n")

    # eigen centrality
    print("START  |  Computing eigen centrality...")
    ec = eigenCentrality(graph)
    if type(ec) is not list: ec = ec.scores()
    saveToFile(datasets[index][0] + "_eigen_centrality", ec)
    print("DONE   |  Eigen centrality computed\n")

    # betweenness centrality
    print("START  |  Computing betweenness centrality...")
    bc = betweennessCentrality(graph)
    if type(bc) is not list: bc = bc.scores()
    saveToFile(datasets[index][0] + "_betweenness_centrality", bc)
    print("DONE   |  Betweenness centrality computed\n")

    # traingles
    print("START  |  Computing traingles...")
    triangles = countTriangles(graph)
    saveToFile(datasets[index][0] + "_triangles", triangles)
    print("DONE   |  Triangles saved\n")

    #        _       _       
    #  _ __ | | ___ | |_ ___ 
    # | '_ \| |/ _ \| __/ __|
    # | |_) | | (_) | |_\__ \
    # | .__/|_|\___/ \__|___/
    # |_|  

    # scatter plot degree centrality (x) and clustering coefficient (y)
    print("START  |  Plotting combined metrics...")
    plotCombinedMetrics(datasets[index][0] + "Scatter" , dc, cc)
    print("DONE   |  Metrics PLot saved to file\n")

    # histogram
    print("START  |  Plotting and saving histograms...")
    plotHistogram(datasets[index][0] + "DCHist", dc, "Degree Centrality")
    plotHistogram(datasets[index][0] + "CCHist", cc, "Clustering Coefficient")
    plotHistogram(datasets[index][0] + "ECHist", ec, "Eigen Centrality")
    plotHistogram(datasets[index][0] + "BCHist", bc, "Betweenness Centrality")
    plotHistogram(datasets[index][0] + "TrianglesHist", triangles, "Triangles")
    print("DONE   |  Histograms saved\n")

    # compute mean radar chart
    print("START  |  Computing mean radar chart...")
    plotRadarChart(datasets[index][0] + "RadarChart", [dc, cc, ec, bc, triangles])
    print("DONE   |  Mean radar chart computed\n")   

    
if __name__ == "__main__":
    main()