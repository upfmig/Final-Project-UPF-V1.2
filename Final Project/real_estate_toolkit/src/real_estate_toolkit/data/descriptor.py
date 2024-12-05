from dataclasses import dataclass
from typing import Dict, List, Tuple, Union
import statistics

@dataclass
class Descriptor:
    """Class for describing real estate data."""
    data: List[Dict[str, Union[str, float, None]]]
    
    def none_ratio(self, columns: List[str] = "all") -> Dict[str, float]:
        """Compute the ratio of None values per column."""
        if columns == "all":
            columns = list(self.data[0].keys())  # Get all columns if 'all' is provided
        
        ratios = {}
        for column in columns:
            if column not in self.data[0]:
                raise ValueError(f"Column '{column}' does not exist in the data.")
            
            total = len(self.data)
            none_count = sum(1 for row in self.data if row[column] is None)
            ratios[column] = none_count / total
            
        return ratios

    def average(self, columns: List[str] = "all") -> Dict[str, float]:
        """Compute the average value for numeric columns."""
        if columns == "all":
            columns = [col for col in self.data[0].keys() if isinstance(self.data[0][col], (int, float))]
        
        averages = {}
        for column in columns:
            if column not in self.data[0]:
                raise ValueError(f"Column '{column}' does not exist in the data.")
            
            if not all(isinstance(row[column], (int, float)) for row in self.data):
                raise ValueError(f"Column '{column}' is not numeric.")
            
            values = [row[column] for row in self.data if row[column] is not None]
            averages[column] = sum(values) / len(values)
            
        return averages

    def median(self, columns: List[str] = "all") -> Dict[str, float]:
        """Compute the median value for numeric columns."""
        if columns == "all":
            columns = [col for col in self.data[0].keys() if isinstance(self.data[0][col], (int, float))]
        
        medians = {}
        for column in columns:
            if column not in self.data[0]:
                raise ValueError(f"Column '{column}' does not exist in the data.")
            
            if not all(isinstance(row[column], (int, float)) for row in self.data):
                raise ValueError(f"Column '{column}' is not numeric.")
            
            values = [row[column] for row in self.data if row[column] is not None]
            medians[column] = statistics.median(values)
            
        return medians

    def percentile(self, columns: List[str] = "all", percentile: int = 50) -> Dict[str, float]:
        """Compute the percentile value for numeric columns."""
        if columns == "all":
            columns = [col for col in self.data[0].keys() if isinstance(self.data[0][col], (int, float))]
        
        percentiles = {}
        for column in columns:
            if column not in self.data[0]:
                raise ValueError(f"Column '{column}' does not exist in the data.")
            
            if not all(isinstance(row[column], (int, float)) for row in self.data):
                raise ValueError(f"Column '{column}' is not numeric.")
            
            values = [row[column] for row in self.data if row[column] is not None]
            percentiles[column] = statistics.quantiles(values, n=100)[percentile - 1]
            
        return percentiles

    def type_and_mode(self, columns: List[str] = "all") -> Dict[str, Union[Tuple[str, float], Tuple[str, str]]]:
        """Compute the mode for variables and return their type."""
        if columns == "all":
            columns = list(self.data[0].keys())
        
        types_and_modes = {}
        for column in columns:
            if column not in self.data[0]:
                raise ValueError(f"Column '{column}' does not exist in the data.")
            
            values = [row[column] for row in self.data if row[column] is not None]
            
            # Determine type
            if all(isinstance(val, (int, float)) for val in values):
                var_type = "numeric"
                mode = statistics.mode(values)
            else:
                var_type = "categorical"
                mode = statistics.mode(values)
            
            types_and_modes[column] = (var_type, mode)
            
        return types_and_modes