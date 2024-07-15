import yaml

def load_config(path="multi_agent_bot/configs/configs.yaml"):
    with open(path, "r") as file:
        config = yaml.safe_load(file)
    return config