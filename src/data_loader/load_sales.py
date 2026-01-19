import pandas as pd


def load_sales_data(file_path: str) -> pd.DataFrame:
    """
    Load sales data from CSV file and parse date column.
    """
    df = pd.read_csv(file_path, parse_dates=["date"])
    return df
