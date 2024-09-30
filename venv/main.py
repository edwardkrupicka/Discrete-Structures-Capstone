import json
import networkx as nx
import matplotlib.pyplot as plt

# Lets load the JSON dataset!
def load_data():
    file_path = 'SocialNetworkData_10K.json'

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the file path.")
        data = {}
        
    return data

def create_nx_graph(data):
    G = nx.Graph() # Initialize graph

    # add nodes and attributes
    for user_id, user_data in data.items():
        G.add_node(user_id, **user_data)

    # add edges based on connections

    for user_id, user_data in data.items():
        for connection in user_data['connections']:
            G.add_edge(user_id, str(connection))

    return G

def basic_analysis(G):
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Average degree: {sum(dict(G.degree()).values()) / G.number_of_nodes():.2f}")

def visualize_graph(G, num_nodes=100):
    subgraph = nx.subgraph(G, list(G.nodes())[:num_nodes])
    pos = nx.spring_layout(subgraph)
    nx.draw(subgraph, pos, with_labels=False, node_size=30)
    plt.title(f"subset of Social Network ({num_nodes} nodes)")
    plt.show()

def main():
    data = load_data()

    if data:
        G = create_nx_graph(data)
        basic_analysis(G)

        visualize_graph(G, num_nodes=100)

if __name__ == '__main__':
    main()


