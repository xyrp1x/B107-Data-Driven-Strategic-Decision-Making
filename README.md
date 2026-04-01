# Reddit Social Network Analysis Project

This project analyzes the Reddit Hyperlink Network Dataset from SNAP (Stanford Network Analysis Project).

## Dataset
Original source: https://snap.stanford.edu/data/soc-RedditHyperlinks.html

### Network definition
- Nodes: subreddits
- Edges: hyperlink references from one subreddit to another
- Type: directed graph

## Research question
Does the Reddit subreddit interaction network follow a scale-free structure similar to a Barabási–Albert graph, and can influential subreddits be identified using centrality measures?

## Assignment requirements covered
- Network construction
- Degree distribution analysis
- Connected components analysis
- Path analysis
- Clustering coefficient and density
- Centrality analysis
- Comparison with ER, BA, and WS graphs
- Open research question

## Project structure
- src/analysis.py — main analysis pipeline
- data/download_dataset.py — dataset downloader
- outputs/ — generated results
- report_template.md — report draft you can adapt
- requirements.txt — dependencies

## How to run
pip install -r requirements.txt
python data/download_dataset.py
python src/analysis.py

## Outputs generated
- outputs/degree_distribution.png
- outputs/comparison_metrics.csv
- outputs/top_degree_centrality.csv
- outputs/top_betweenness_centrality.csv
- outputs/top_closeness_centrality.csv
- outputs/summary.txt

## GitHub note
Your final PDF report should include the link to your GitHub repository.
