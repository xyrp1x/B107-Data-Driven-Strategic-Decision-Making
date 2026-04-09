# Social Network Analysis Report: Reddit Hyperlink Network

## GitHub Repository
[Paste your GitHub repository link here]

## 1. Introduction
This report analyzes a Reddit hyperlink interaction network constructed from the Reddit Hyperlink Network Dataset published by the Stanford Network Analysis Project (SNAP). In this network, nodes represent subreddits and edges represent hyperlink references between communities. The aim of the project is to investigate the structural properties of the network and compare them with three well-known random graph models: Erdős–Rényi (ER), Barabási–Albert (BA), and Watts–Strogatz (WS).

The research question addressed in this report is:
**Does the Reddit subreddit interaction network follow a scale-free structure similar to a BA graph, and can influential subreddits be identified using centrality measures?**

## 2. Network Construction
The network was built using the Reddit Hyperlink Network Dataset. Each node represents a subreddit, while each directed edge captures a hyperlink reference from one subreddit to another. The graph contains more than the minimum required number of nodes and therefore satisfies the assignment requirement. Additional edge information is preserved from the dataset and may be used for further interpretation.

Include here:
- number of nodes
- number of edges
- whether graph is directed
- any extra attributes available

## 3. Network Analysis

### 3.1 Degree Distribution
Discuss the degree distribution and whether hubs are present. Insert the degree distribution figure generated in `outputs/degree_distribution.png`.

### 3.2 Connected Components
Report the number of connected components and the size of the giant component.

### 3.3 Path Analysis
Discuss average shortest path length and diameter of the giant component.

### 3.4 Clustering Coefficient and Density
Present and interpret:
- average clustering coefficient
- graph density

### 3.5 Centrality Analysis
Use the generated CSV files to identify the most influential subreddits:
- degree centrality
- betweenness centrality
- closeness centrality

## 4. Comparison with ER, BA and WS Graphs
Using the comparison table in `outputs/comparison_metrics.csv`, compare the real Reddit network with:
- Erdős–Rényi graph
- Barabási–Albert graph
- Watts–Strogatz graph

Discuss:
- which model is closest to the real network
- whether the real network is scale-free, random, or small-world
- how clustering and path length differ across models

## 5. Open Question
Research question:
**Does the Reddit subreddit interaction network follow a scale-free structure similar to a BA graph, and can influential subreddits be identified using centrality measures?**

Suggested answer structure:
- explain whether hubs exist
- compare real network degree distribution to BA
- discuss whether centrality reveals structurally important subreddits
- explain whether the highest-degree nodes also have high betweenness

## 6. Conclusion
Summarize:
- how the network was constructed
- the most important structural findings
- which comparison graph best matches the real Reddit network
- the answer to the research question
