from pathlib import Path
from typing import List, Dict, Any
from src.real_estate_toolkit.data.loader import DataLoader
from src.real_estate_toolkit.data.cleaner import Cleaner
from src.real_estate_toolkit.data.descriptor import Descriptor


data_path = Path("src/data/train.csv")
loader = DataLoader(data_path)
required_columns = ["Id", "SalePrice", "LotArea", "YearBuilt", "BedroomAbvGr"]
loader.validate_columns(required_columns)

def test_data_loading_and_cleaning():
    """Test data loading and cleaning functionality"""
    # Test data loading
    data_path = Path("real_estate_toolkit/src/data/train.csv")
    loader = DataLoader(data_path)
    
    # Test column validation
    required_columns = ["Id", "SalePrice", "LotArea", "YearBuilt", "BedroomAbvGr"]
    assert loader.validate_columns(required_columns), "Required columns missing from dataset"
    
    # Load and test data format
    data = loader.load_data_from_csv()
    assert isinstance(data, list), "Data should be returned as a list"
    assert all(isinstance(row, dict) for row in data), "Each row should be a dictionary"
    
    # Test data cleaning
    cleaner = Cleaner(data)
    cleaner.rename_with_best_practices()
    cleaned_data = cleaner.na_to_none()
    
    # Verify cleaning results
    assert all(key.islower() and "_" in key for key in cleaned_data[0].keys()), "Column names should be in snake_case"
    assert all(val is None or isinstance(val, (str, int, float)) for row in cleaned_data for val in row.values()), \
        "Values should be None or basic types"
    
    return cleaned_data