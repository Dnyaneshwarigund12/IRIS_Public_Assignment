import os
import pandas as pd

def load_excel(file_path: str) -> dict:
    """Reads Excel file and returns dictionary of DataFrames keyed by sheet name."""
    if not os.path.exists(file_path):
        raise FileNotFoundError("Excel file not found.")

    try:
        excel_data = pd.read_excel(file_path, sheet_name=None)
        if not excel_data:
            raise ValueError("Excel file is empty or unreadable.")
        return excel_data
    except Exception as e:
        raise RuntimeError(f"Failed to load Excel file: {e}")
