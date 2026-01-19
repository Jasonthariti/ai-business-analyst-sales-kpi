import pandas as pd


def calculate_monthly_trend(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate monthly sales trend and growth rate.
    """
    monthly_summary = (
        df
        .assign(month=df["date"].dt.to_period("M").astype(str))
        .groupby("month", as_index=False)
        .agg(
            total_revenue=("revenue", "sum"),
            total_cost=("cost", "sum")
        )
    )

    monthly_summary["total_profit"] = (
        monthly_summary["total_revenue"] - monthly_summary["total_cost"]
    )

    monthly_summary["revenue_growth_rate"] = (
        monthly_summary["total_revenue"]
        .pct_change()
        .fillna(0)
        .round(2)
    )

    return monthly_summary