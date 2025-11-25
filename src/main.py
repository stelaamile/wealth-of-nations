from src.load_wb_data import load_gdp_per_capita_from_csv
from src.demo_data import load_demo_data, analyze_demo_data, print_countries
import numpy as np
import matplotlib.pyplot as plt

def show_worldbank_preview():
    """
    Load the World Bank GDP per capita dataset using pandas
    and print a clean preview, including:
    - first five rows
    - number of rows
    - column names
    """

    filepath = "data/worldbank_gdp_per_capita.csv"
    df = load_gdp_per_capita_from_csv(filepath)

    print("\n=== WORLD BANK GDP PER CAPITA: PREVIEW ===")
    print(df.head())
    print(f"\nNumber of rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")

    # New: run a simple pandas + numpy analysis
    analyze_worldbank_data(df)

    # New: create and save a plot
    plot_global_gdp_trend(df)

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

def plot_global_gdp_trend(df):
    """
    Plot the global average GDP per capita over time
    and save the figure to the 'data/' directory.

    Args:
        df (pd.DataFrame): Cleaned GDP per capita DataFrame.
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

def main():
    """
    Main entry point for the Wealth of Nations project.

    Runs:
    - demo dataset loading and analysis (pure Python)
    - World Bank dataset loading, cleaning, analysis (pandas + NumPy)
    - GDP trend visualisation (matplotlib)
    """

    print("Welcome to 'The Wealth of Nations' project!")

    filepath = "data/demo_countries.csv"
    data = load_demo_data(filepath)

    if not data:
        print("No data loaded. Exiting program.")
        return

    print("Demo data loaded successfully.")
    print_countries(data)
    analyze_demo_data(data)

    # New: also show the World Bank dataset
    show_worldbank_preview()



if __name__ == "__main__":
    main() 