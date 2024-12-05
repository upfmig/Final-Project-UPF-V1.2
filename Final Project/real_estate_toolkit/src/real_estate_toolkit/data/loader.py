from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Any
import csv

@dataclass
class DataLoader:
    """Class for loading and basic processing of real estate data."""
    data_path = Path("real_estate_toolkit/src/data/data_files")
    data_path: Path
    
    def load_data_from_csv(self, file_name: str) -> List[Dict[str, Any]]:
        """Load data from a specific CSV file (train.csv or test.csv) into a list of dictionaries."""
        data = []
        file_path = self.data_path / file_name  # Combine the path and the file name
        
        # Open the specified CSV file
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                data.append(row)  # Add each row (dictionary) to the data list
        
        return data
    
    def validate_columns(self, file_name: str, required_columns: List[str]) -> bool:
        """Validate that all required columns are present in the dataset (train.csv or test.csv)."""
        file_path = self.data_path / file_name  # Combine the path and the file name
        
        # Open the specified CSV file to check the header
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Get the header (first row)
        
        # Check if all required columns are in the header
        return all(col in header for col in required_columns)
    


