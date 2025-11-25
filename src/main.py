from src.load_wb_data import load_gdp_per_capita_from_csv
from src.demo_data import load_demo_data, analyze_demo_data, print_countries
from src.analysis import analyze_worldbank_data
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