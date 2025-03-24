from pathlib import Path
import pandas as pd
import numpy as np

# Define the file path variable at the top
FILE_PATH: Path = Path(__file__).parent / "data" / "Walmart_customer_purchases.csv"

class DataExploration:
    """Data exploration class"""
    def __init__(self, file_path: Path):
        self.file_path = file_path
        print(self.file_path)

class DataCleaning:...

if __name__ == '__main__':
    # Example usage
    data_exploration = DataExploration(FILE_PATH)

    # Here is a suggested project structure for your project:
    # 
    # everythingdata_project/
    # ├── data/                # Place your data files here (e.g., Walmart_customer_purchases.csv)
    # ├── src/                 # Source code directory
    # │   ├── main.py          # Main script
    # │   ├── modules/         # Optional: Place additional Python modules here
    # ├── tests/               # Place your test scripts here
    # ├── README.md            # Optional: Project documentation
    # ├── requirements.txt     # Optional: List of dependencies
    # ├── .gitignore           # Optional: Git ignore file
    # 
    # Notes:
    # - The `data` directory should be at the root level of the project, not inside `src`.
    # - The `tests` directory should also be at the root level for better organization.
    # - Update the `FILE_PATH` in your code to reflect the new location of the `data` directory:
    #   FILE_PATH: Path = Path(__file__).parent.parent / "data" / "Walmart_customer_purchases.csv"
    