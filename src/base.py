from pathlib import Path
import pandas as pd
import numpy as np


FILE_PATH: Path = Path(__file__).parent / "data" / "Walmart_customer_purchases.csv"

class DataExploration:
    """Data exploration class"""
    def __init__(self, file_path: Path):
        self.file_path = file_path
        print(self.file_path)

class DataCleaning:...

if __name__ == '__main__':
    data_exploration = DataExploration(FILE_PATH)
