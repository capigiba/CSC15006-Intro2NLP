import yaml
import os

class Config:
    def __init__(self, config_path='config.yaml'):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file '{config_path}' not found.")
        
        with open(config_path, 'r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file)
        
    def get(self, key, default=None):
        return self.config.get(key, default)
