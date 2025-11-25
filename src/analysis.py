"""
Analysis functions for the World Bank GDP dataset.

This module contains all numerical and statistical analysis:
- global stats
- top regions
- growth analysis (to be added)
- inequality analysis (to be added)
"""

import numpy as np
import pandas as pd


def analyze_worldbank_data(df):
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
    for _, row in top5.iterrows():
        print(f" - {row['region_name']}: {row['gdp_per_capita']:,.2f} USD")
