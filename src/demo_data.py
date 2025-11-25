"""
Utilities for loading and analyzing the small demo CSV dataset
using only base Python (no pandas).

This module is separate from the main World Bank analysis to keep
the project structure clean and modular.
"""


def load_demo_data(filepath):
    """
    Load a small CSV file using basic Python methods (no pandas).

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        list[dict]: A list of dictionaries, one per country.
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
    Perform simple analysis on the demo dataset using pure Python.

    Computes:
    - average GDP per capita
    - the country with the highest life expectancy
    - list of countries with above-average GDP per capita

    Args:
        countries (list[dict]): Dataset loaded by load_demo_data().
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
    print("\n=== ANALYSIS RESULTS (DEMO DATA) ===")
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
    print("\nCountries in the demo dataset:")
    print(f"(Total: {len(countries)} countries)\n")

    for row in countries:
        country = row["country"]
        year = row["year"]
        gdp = row["gdp_per_capita"]
        life = row["life_expectancy"]
        print(f" - {country} ({year}) | GDP per capita: {gdp} | Life expectancy: {life}")
