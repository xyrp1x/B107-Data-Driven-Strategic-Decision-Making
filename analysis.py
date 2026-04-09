import os
import urllib.request
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

DATA_DIR = "data"
OUTPUT_DIR = "outputs"
DATA_FILE = os.path.join(DATA_DIR, "soc-redditHyperlinks-body.tsv")
DATA_URL = "https://snap.stanford.edu/data/soc-redditHyperlinks-body.tsv"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_dataset():
    if os.path.exists(DATA_FILE):
        print(f"Dataset already exists: {DATA_FILE}")
        return
    print("Downloading dataset...")
    urllib.request.urlretrieve(DATA_URL, DATA_FILE)
    print("Download complete.")

def load_dataset():
    return pd.read_csv(DATA_FILE, sep="\t")

def build_graph(df):
    return nx.from_pandas_edgelist(
        df,
        source="SOURCE_SUBREDDIT",
        target="TARGET_SUBREDDIT",
        edge_attr=True,
        create_using=nx.DiGraph()
    )

def save_degree_distribution(G):
    degrees = [d for _, d in G.degree()]
    plt.figure(figsize=(8, 5))
    plt.hist(degrees, bins=50, edgecolor="black")
    plt.title("Degree Distribution of Reddit Hyperlink Network")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "degree_distribution.png"))
    plt.close()

def compute_metrics(G):
    undirected = G.to_undirected()
    largest_cc_nodes = max(nx.connected_components(undirected), key=len)
    giant = undirected.subgraph(largest_cc_nodes).copy()

    metrics = {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "density": nx.density(G),
        "average_clustering": nx.average_clustering(undirected),
        "num_connected_components": nx.number_connected_components(undirected),
        "largest_component_size": giant.number_of_nodes(),
        "average_shortest_path_length_giant": nx.average_shortest_path_length(giant),
        "diameter_giant": nx.diameter(giant),
        "average_degree": sum(dict(G.degree()).values()) / G.number_of_nodes()
    }

    degree_c = nx.degree_centrality(G)
    betweenness_c = nx.betweenness_centrality(G, k=50, seed=42)
    closeness_c = nx.closeness_centrality(G.subgraph(list(G.nodes())[:500]))


    top_degree = sorted(degree_c.items(), key=lambda x: x[1], reverse=True)[:10]
    top_betweenness = sorted(betweenness_c.items(), key=lambda x: x[1], reverse=True)[:10]
    top_closeness = sorted(closeness_c.items(), key=lambda x: x[1], reverse=True)[:10]

    return metrics, top_degree, top_betweenness, top_closeness

def generate_comparison_graphs(n, m):
    er = nx.gnm_random_graph(n, m, seed=42)

    ba_m = max(1, min(n - 1, round(m / n)))
    ba = nx.barabasi_albert_graph(n, ba_m, seed=42)

    avg_degree = max(2, round((2 * m) / n))
    if avg_degree % 2 == 1:
        avg_degree += 1
    avg_degree = min(avg_degree, n - 1 if (n - 1) % 2 == 0 else n - 2)
    ws = nx.watts_strogatz_graph(n, avg_degree, 0.3, seed=42)

    return {"ER": er, "BA": ba, "WS": ws}

def summarize_graph(name, G):
    UG = G.to_undirected() if G.is_directed() else G
    largest_cc_nodes = max(nx.connected_components(UG), key=len)
    giant = UG.subgraph(largest_cc_nodes).copy()
    return {
        "Graph": name,
        "Nodes": G.number_of_nodes(),
        "Edges": G.number_of_edges(),
        "Density": nx.density(G),
        "Avg_Clustering": nx.average_clustering(UG),
        "Connected_Components": nx.number_connected_components(UG),
        "Largest_Component": giant.number_of_nodes(),
        "Avg_Path_Length_Giant": nx.average_shortest_path_length(giant),
    }

def main():
    download_dataset()
    df = load_dataset()
    G = build_graph(df)

    save_degree_distribution(G)
    metrics, top_degree, top_betweenness, top_closeness = compute_metrics(G)
    comparison_graphs = generate_comparison_graphs(G.number_of_nodes(), G.number_of_edges())

    import pandas as pd
    rows = [summarize_graph("Real Reddit Network", G)]
    for name, graph in comparison_graphs.items():
        rows.append(summarize_graph(name, graph))
    pd.DataFrame(rows).to_csv(os.path.join(OUTPUT_DIR, "comparison_metrics.csv"), index=False)

    pd.DataFrame(top_degree, columns=["Node", "Degree_Centrality"]).to_csv(
        os.path.join(OUTPUT_DIR, "top_degree_centrality.csv"), index=False
    )
    pd.DataFrame(top_betweenness, columns=["Node", "Betweenness_Centrality"]).to_csv(
        os.path.join(OUTPUT_DIR, "top_betweenness_centrality.csv"), index=False
    )
    pd.DataFrame(top_closeness, columns=["Node", "Closeness_Centrality"]).to_csv(
        os.path.join(OUTPUT_DIR, "top_closeness_centrality.csv"), index=False
    )

    with open(os.path.join(OUTPUT_DIR, "summary.txt"), "w", encoding="utf-8") as f:
        f.write("REDDIT NETWORK SUMMARY\n")
        for k, v in metrics.items():
            f.write(f"{k}: {v}\n")
        f.write("\nTop 10 by Degree Centrality\n")
        for item in top_degree:
            f.write(f"{item}\n")
        f.write("\nTop 10 by Betweenness Centrality\n")
        for item in top_betweenness:
            f.write(f"{item}\n")
        f.write("\nTop 10 by Closeness Centrality\n")
        for item in top_closeness:
            f.write(f"{item}\n")

    print("Analysis complete. Check the outputs/ folder.")

if __name__ == "__main__":
    main()
