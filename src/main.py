from src.load_wb_data import load_gdp_per_capita_from_csv
import numpy as np
import matplotlib.pyplot as plt

def load_demo_data(filepath):
    """
    Load a small CSV file using basic Python.
    Returns a list of dictionaries.
    """
    countries = []  # store all our rows as dictionaries

    try:
        # open the file in read mode
        with open(filepath, "r") as file:
            lines = file.readlines()

            # first line = column names
            header = lines[0].strip().split(",")

            # for each line after the header
            for line in lines[1:]:
                values = line.strip().split(",")

                # build a dictionary: column_name → value
                row_dict = {header[i]: values[i] for i in range(len(header))}
                countries.append(row_dict)

    except FileNotFoundError:
        print("Error: file not found.")

    return countries


def analyze_demo_data(countries):
    """
    Do a very simple analysis on the demo data:
    - compute average GDP per capita
    - find the country with the highest life expectancy
    - list countries with GDP per capita above the average
    """
    if not countries:
        print("No data to analyze.")
        return

    # --- average GDP per capita ---
    total_gdp = 0
    count = 0

    for country in countries:
        # values from CSV are strings -> convert to int
        gdp_str = country["gdp_per_capita"]
        gdp_value = int(gdp_str)
        total_gdp += gdp_value
        count += 1

    average_gdp = total_gdp / count

    # --- country with max life expectancy ---
    max_life = None
    max_country = None

    for country in countries:
        life_str = country["life_expectancy"]
        life_value = float(life_str)

        if (max_life is None) or (life_value > max_life):
            max_life = life_value
            max_country = country["country"]

    # --- countries with GDP per capita above average ---
    above_average_countries = []
    for country in countries:
        gdp_value = int(country["gdp_per_capita"])
        if gdp_value > average_gdp:
            above_average_countries.append(country["country"])

    # ---- printing results ----
    print("\n=== ANALYSIS RESULTS ===")
    print(f"Average GDP per capita: {average_gdp:,.2f} USD")
    print(f"Highest life expectancy: {max_life} years ({max_country})")

    print("\nCountries with GDP per capita ABOVE the average:")
    if above_average_countries:
        for name in above_average_countries:
            print(f" - {name}")
    else:
        print(" (none)")

    print("========================\n")


def print_countries(countries):
    """
    Print a readable summary of all countries in the dataset.
    """
    print("\nCountries in the dataset:")
    print(f"(Total: {len(countries)} countries)\n")

    for row in countries:
        country = row["country"]
        year = row["year"]
        gdp = row["gdp_per_capita"]
        life = row["life_expectancy"]
        print(f" - {country} ({year}) | GDP per capita: {gdp} | Life expectancy: {life}")

def show_worldbank_preview():
    """
    Load the World Bank GDP per capita CSV with pandas
    and print a small preview and basic info.
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
    Do a simple analysis on the World Bank GDP per capita data using
    pandas and numpy.

    - compute global mean and standard deviation of GDP per capita
    - find the most recent year in the dataset
    - list the top 5 regions by GDP per capita in that most recent year
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
    and save it as an image in the data/ folder.
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