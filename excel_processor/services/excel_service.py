from typing import List, Dict, Any
from utils.file_loader import load_excel
import pandas as pd

EXCEL_PATH = "Data/capbudg.xls"


def get_all_tables() -> List[str]:
    sheets = load_excel(EXCEL_PATH)
    return list(sheets.keys())


def get_table_rows(table_name: str) -> Dict[str, Any]:
    sheets = load_excel(EXCEL_PATH)
    if table_name not in sheets:
        raise ValueError("Table name not found in Excel.")

    df = sheets[table_name].dropna(how="all")
    if df.empty or df.shape[1] < 1:
        raise ValueError("Selected table is empty or malformed.")

    row_names = df.iloc[:, 0].dropna().tolist()
    return {
        "table_name": table_name,
        "row_names": row_names
    }


def get_row_sum(table_name: str, row_name: str) -> Dict[str, Any]:
    sheets = load_excel(EXCEL_PATH)
    if table_name not in sheets:
        raise ValueError("Table name not found in Excel.")

    df = sheets[table_name].dropna(how="all")
    if df.empty or df.shape[1] < 2:
        raise ValueError("Selected table has no data.")

    matched_rows = df[df.iloc[:, 0] == row_name]
    if matched_rows.empty:
        raise ValueError("Row name not found in the table.")

    row_data = matched_rows.iloc[0, 1:]
    numeric_data = pd.to_numeric(row_data, errors='coerce')

    if numeric_data.isnull().all():
        raise ValueError("Row contains no numeric data.")

    total_sum = numeric_data.sum()
    return {
        "table_name": table_name,
        "row_name": row_name,
        "sum": total_sum
    }
