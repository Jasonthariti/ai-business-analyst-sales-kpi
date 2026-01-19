import pandas as pd


def calculate_product_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate product-level KPIs for Sales Manager.
    """
    product_summary = (
        df
        .groupby("product", as_index=False)
        .agg(
            total_revenue=("revenue", "sum"),
            total_cost=("cost", "sum"),
            total_quantity=("quantity", "sum")
        )
    )

    product_summary["total_profit"] = (
        product_summary["total_revenue"] - product_summary["total_cost"]
    )

    product_summary["profit_margin"] = (
        product_summary["total_profit"] / product_summary["total_revenue"]
    )

    return product_summary.round(2)
