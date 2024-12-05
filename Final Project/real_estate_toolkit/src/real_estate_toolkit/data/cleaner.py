from dataclasses import dataclass
from typing import Dict, List, Any
import re

@dataclass
class Cleaner:
    """Class for cleaning real estate data."""
    data: List[Dict[str, Any]]

    def rename_with_best_practices(self) -> None:
        """Rename the columns with best practices (e.g., snake_case, very descriptive name)."""
        # Iterate through each dictionary (row) in data
        for row in self.data:
            # Create a new dictionary with renamed keys
            new_row = {}
            for column in row.keys():
                # Convert column name to snake_case using regular expressions
                new_column = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', column)  # CamelCase to snake_case
                new_column = re.sub(r'[^a-z0-9_]', '_', new_column)  # Replace non-alphanumeric characters with underscores
                new_column = new_column.lower()  # Convert to lowercase
                new_row[new_column] = row[column]
            
            # Update the row with the new column names
            row.clear()
            row.update(new_row)

    def na_to_none(self) -> List[Dict[str, Any]]:
        """Replace 'NA' with None in all values with 'NA' in the dictionary."""
        for row in self.data:
            for column in row:
                # Replace "NA" string with None
                if row[column] == "NA":
                    row[column] = None
        return self.data