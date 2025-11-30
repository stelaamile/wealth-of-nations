import pandas as pd
from src.load_wb_data import load_gdp_data # CRITICAL: Import the unified loader
from src.demo_data import load_demo_data, analyze_demo_data, print_countries
from src.analysis import analyze_worldbank_data
from src.visualization import plot_global_gdp_trend
from src.models import GDPRegion

def show_worldbank_analysis():
    """
    Load the World Bank GDP per capita dataset using the unified loader
    (API/filtering) and execute the full analysis pipeline.
    """
    
    # 1. Load data using the unified, filtered function (API is default)
    df = load_gdp_data(use_api=True) # Use the correct, filtered function

    if df is None or df.empty:
        print("\nFATAL ERROR: World Bank data could not be loaded or is empty.")
        return

    print("\n\n=== WORLD BANK DATASET LOADED ===")
    print(f"Number of clean country-year observations: {len(df):,}")
    print(f"Columns: {list(df.columns)}\n")

    # 2. Run the main analysis (prints stats to terminal)
    analyze_worldbank_data(df)

    # 3. Create and save a plot (Visualization C6)
    plot_global_gdp_trend(df)

    # --- 4. OOP Demo: Build and inspect GDPRegion objects ---
    # Sample a few rows for the demonstration
    sample_rows = df.sample(5)

    regions = [
        GDPRegion(
            region_code=row.region_code,
            region_name=row.region_name,
            year=int(row.year),
            gdp_per_capita=float(row.gdp_per_capita),
        )
        for row in sample_rows.itertuples(index=False)
    ]

    print("\n=== Example GDPRegion objects (OOP Demo) ===")
    for r in regions:
        # Uses __repr__ and is_high_income() methods
        print(f"{r} | high income: {r.is_high_income()}")


def main():
    """
    Main entry point for the Wealth of Nations project.

    Runs:
    - demo dataset loading and analysis (pure Python)
    - World Bank dataset loading, cleaning, analysis (pandas + NumPy)
    - GDP trend visualisation (matplotlib)
    """

    print("Welcome to 'The Wealth of Nations' project! (CLI Mode)")

    # 1. Run pure Python demo (C1)
    filepath = "data/demo_countries.csv"
    data = load_demo_data(filepath)

    if not data:
        print("Demo data not loaded. Skipping pure Python analysis.")
    else:
        print("\n--- Running Pure Python Demo ---")
        print_countries(data)
        analyze_demo_data(data)

    # 2. Run the World Bank analysis pipeline (C3, C4, C5, C6)
    show_worldbank_analysis()


if __name__ == "__main__":
    main()
    