import json
import os

def load_test_data(filename: str):
    """
    Load JSON test data from resources/test_data/<filename>.
    Returns the parsed Python object (list or dict).
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
    file_path = os.path.join(base_dir, 'resources', 'test_data', filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
