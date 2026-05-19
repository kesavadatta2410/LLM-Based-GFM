from torch_geometric.datasets import Planetoid

def load_cora_dataset():

    dataset = Planetoid(
        root="data/Cora",
        name="Cora"
    )

    data = dataset[0]

    return dataset, data