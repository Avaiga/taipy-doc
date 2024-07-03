import taipy as tp
from taipy import Config

if __name__ == "__main__":
    # Configure a global data node
    dataset_cfg = Config.configure_data_node("my_dataset", scope=tp.Scope.GLOBAL)

    # Instantiate a global data node
    dataset = tp.create_global_data_node(dataset_cfg)

    # Retrieve the list of all data nodes
    all_data_nodes = tp.get_data_nodes()

    # Write the data
    dataset.write("Hello, World!")

    # Read the data
    print(dataset.read())
