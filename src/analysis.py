import numpy as np
import pandas as pd


def analyze_worldbank_data(df: pd.DataFrame) -> None:
    """
    Perform pandas and NumPy-based analysis on the World Bank dataset.

    Computes:
    - global mean GDP per capita
    - global standard deviation
    - most recent year in the dataset
    - top 5 regions by GDP per capita for that year

    Args:
        df (pd.DataFrame): Cleaned DataFrame returned by the loader.
    """
    # Drop missing values just in case
    df = df.dropna(subset=["gdp_per_capita"])

    # Global stats with numpy
    gdp_values = df["gdp_per_capita"].values
    global_mean = np.mean(gdp_values)
    global_std = np.std(gdp_values)

    print("\n=== WORLD BANK GDP: GLOBAL STATS ===")
    print(f"Global mean GDP per capita: {global_mean:,.2f} USD")
    print(f"Global std dev GDP per capita: {global_std:,.2f} USD")

    # Most recent year in the dataset
    latest_year = df["year"].max()
    latest_df = df[df["year"] == latest_year]

    # Top 5 regions in that year
    top5 = latest_df.nlargest(5, "gdp_per_capita")[["region_name", "gdp_per_capita"]]

    print(f"\nTop 5 regions in {latest_year} by GDP per capita:")
    for i in range(len(top5)):
        region = top5.iloc[i]["region_name"]
        gdp = top5.iloc[i]["gdp_per_capita"]
        print(f" - {region}: {gdp:,.2f} USD")


# ---------- New helper functions for Streamlit ----------

def compute_global_yearly_average(df: pd.DataFrame) -> pd.Series:
    """Return a Series with the global average GDP per capita for each year."""
    return df.groupby("year")["gdp_per_capita"].mean().sort_index()


def summarize_global_trend(df: pd.DataFrame) -> dict:
    """
    Compute a simple summary of the global GDP per capita trend.

    Returns:
        dict with keys:
            first_year, last_year, first_value, last_value, growth_pct
    """
    yearly_avg = compute_global_yearly_average(df)

    first_year = int(yearly_avg.index.min())
    last_year = int(yearly_avg.index.max())
    first_value = float(yearly_avg.loc[first_year])
    last_value = float(yearly_avg.loc[last_year])

    growth_pct = (last_value / first_value - 1) * 100

    return {
        "first_year": first_year,
        "last_year": last_year,
        "first_value": first_value,
        "last_value": last_value,
        "growth_pct": growth_pct,
    }


def compute_region_vs_world(df: pd.DataFrame, region_name: str) -> pd.DataFrame:
    """
    Build a DataFrame with GDP per capita for a given region
    and the global average for each year.

    Columns:
        year, region_gdp, world_gdp
    """
    # Global average
    global_series = compute_global_yearly_average(df)

    # Selected region
    region_df = df[df["region_name"] == region_name]
    region_series = (
        region_df.groupby("year")["gdp_per_capita"]
        .mean()
        .reindex(global_series.index)
    )

    combined = pd.DataFrame(
        {
            "year": global_series.index,
            "region_gdp": region_series.values,
            "world_gdp": global_series.values,
        }
    )

    return combined


def compute_rich_poor_gap(df: pd.DataFrame) -> pd.DataFrame:
    """
    For each year, find the richest and poorest regions and compute the gap.

    Returns a DataFrame with columns:
        year, richest_region, poorest_region,
        richest_gdp, poorest_gdp, gap
    """
    # Group by year and region, take mean in case there are multiple entries
    grouped = df.groupby(["year", "region_name"])["gdp_per_capita"].mean().reset_index()

    records = []
    for year, subset in grouped.groupby("year"):
        richest_row = subset.loc[subset["gdp_per_capita"].idxmax()]
        poorest_row = subset.loc[subset["gdp_per_capita"].idxmin()]

        records.append(
            {
                "year": int(year),
                "richest_region": richest_row["region_name"],
                "poorest_region": poorest_row["region_name"],
                "richest_gdp": float(richest_row["gdp_per_capita"]),
                "poorest_gdp": float(poorest_row["gdp_per_capita"]),
                "gap": float(richest_row["gdp_per_capita"] - poorest_row["gdp_per_capita"]),
            }
        )

    gap_df = pd.DataFrame(records).sort_values("year")
    return gap_df
