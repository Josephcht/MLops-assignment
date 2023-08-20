import hydra
from omegaconf import DictConfig


@hydra.main(config_path="../config", config_name="main", version_base=None)
def process_data(config: DictConfig):
    """Function to process the data"""

    print(f"Called saved model naem: {config.model.name}")
    print(f"Columns used: {config.process.use_cols}")


if __name__ == "__main__":
    process_data()