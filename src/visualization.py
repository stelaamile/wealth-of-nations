"""
Visualization functions for the Wealth of Nations project.

This module contains all plotting logic.
"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_global_gdp_trend(df: pd.DataFrame) -> None:
    """
    Plot the global average GDP per capita over time
    and save the figure to the 'data/' directory.

    Args:
        df (pd.DataFrame): Cleaned GDP per capita DataFrame,
            with at least 'year' and 'gdp_per_capita' columns.
    """
    # Compute global average per year
    yearly_avg = df.groupby("year")["gdp_per_capita"].mean()

    plt.figure(figsize=(8, 4))
    plt.plot(yearly_avg.index, yearly_avg.values)
    plt.title("Global Average GDP per Capita Over Time")
    plt.xlabel("Year")
    plt.ylabel("GDP per capita (USD)")
    plt.tight_layout()

    # Save the figure to a file
    output_path = "data/global_gdp_trend.png"
    plt.savefig(output_path)
    print(f"\nSaved plot to {output_path}")
