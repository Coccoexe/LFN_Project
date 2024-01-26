# Project of Learning From Network

This repository provides code to compute graph metrics and plot chart to helps with graph analysis.
The original puropouse of this code was to detect similarities and/or differences between human and mouse genes regulatory systems.

### Metrics
- [Degree centrality](https://en.wikipedia.org/wiki/Centrality)
- [Clustering coefficient](https://en.wikipedia.org/wiki/Clustering_coefficient)
- [Betweenness centrality](https://en.wikipedia.org/wiki/Betweenness_centrality)
- [Eigen centrality](https://en.wikipedia.org/wiki/Eigenvector_centrality)
- Triangles

### Plots
- Scatter plot that combines degree and clustering coefficient
- Histogram for each metric
- Radar chart that shows the mean of each metric

## Instructions

### Requirements
- [networkx](https://networkx.org/)
- [networkit](https://networkit.github.io/)
- [matplotlib](https://matplotlib.org/)
- [numpy](https://numpy.org/)

### Main
Depending on python installation is possible to run main file via:
``` 
python main.py
python3 main.py
```
Make sure to have a data folder with at least a dataset otherwise the program won't work. 

You can use setup.py to downlaod tested dataset

### Setup
Setup.py is a file that automatically downloads and prepare the two dataset we used in our project.
```
python setup.py
```

### Contributors
- Alessio Cocco
- Andrea Valentinuzzi
- Giovanni Brejc