import networkx as nx

def build_graph(data):

    G = nx.Graph()

    edge_index = data.edge_index.numpy()

    for i in range(edge_index.shape[1]):

        src = int(edge_index[0][i])
        dst = int(edge_index[1][i])

        G.add_edge(src, dst)

    return G