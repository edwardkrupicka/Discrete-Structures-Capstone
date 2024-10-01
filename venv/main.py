import json
import networkx as nx
import matplotlib.pyplot as plt

# Lets load the JSON dataset!
def load_data():
    file_path = 'SocialNetworkData_10K.json'
    
    try: # the try, opens and loads the JSON file
        with open(file_path, 'r') as f:
            data = json.load(f)
        print("Data loaded successfully.")
    except FileNotFoundError: # the except, if the file can't be found
        print(f"Error: The file '{file_path}' was not found. Please check the file path.")
        data = {} # Sets data as an empty set. This is so when we call this function later, it returns data as false and doesn't try to run the rest of the script
        
    return data # returns the json data with try and empty set with except

# Creates the graph using  NetworkX
def create_nx_graph(data):
    G = nx.Graph() # Initialize graph

    # loops through each user and unpacks their data, then adds this to their node
    for user_id, user_data in data.items():
        G.add_node(user_id, **user_data)

    # add edges based on connections of user nodes
    for user_id, user_data in data.items(): # Outer loop, looks through each user in data
        for connection in user_data['connections']:
            G.add_edge(user_id, str(connection))
            
    # return the graph
    return G

# Print the nodes, edges and the average degree of the graph
def basic_analysis(G):
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Average degree: {sum(dict(G.degree()).values()) / G.number_of_nodes():.2f}")

# Now we use Matplotlib to create a visualization of the graph
def visualize_graph(G, num_nodes=100):
    subgraph = nx.subgraph(G, list(G.nodes())[:num_nodes])
    pos = nx.spring_layout(subgraph)
    nx.draw(subgraph, pos, with_labels=False, node_size=30)
    plt.suptitle(f"Subset of Social Network ({num_nodes} nodes)")
    plt.show()

# Function to execute all the other functions
def main():
    data = load_data()

    if data:
        G = create_nx_graph(data)
        basic_analysis(G)
        visualize_graph(G, num_nodes=100)

if __name__ == '__main__':
    main()


