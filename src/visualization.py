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

# Use Object-Oriented Interface (Creation of fig and ax)
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.set_xticks(yearly_avg.index)
    plt.xticks(rotation=45)
    
    # Plotting is done on the ax object
    ax.plot(yearly_avg.index, yearly_avg.values)
    ax.set_title("Global Average GDP per Capita Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP per capita (USD)")
    
    plt.tight_layout()

    # Save the figure object
    output_path = "data/global_gdp_trend.png"
    fig.savefig(output_path) # Save the figure object (fig)