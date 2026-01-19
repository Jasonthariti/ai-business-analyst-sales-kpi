import pandas as pd


def calculate_sales_kpis(df: pd.DataFrame) -> dict:
    """
    Calculate core sales KPIs for Sales Manager.
    """
    total_revenue = float(df["revenue"].sum())
    total_cost = float(df["cost"].sum())
    total_profit = total_revenue - total_cost

    profit_margin = (
        total_profit / total_revenue if total_revenue > 0 else 0
    )

    return {
        "total_revenue": round(total_revenue, 2),
        "total_profit": round(total_profit, 2),
        "profit_margin": round(profit_margin, 2),
    }
