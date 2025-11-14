def load_demo_data(filepath):
    """
    Load a small CSV file using basic Python.
    Returns a list of dictionaries, one per country.
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

    print("\n=== ANALYSIS RESULTS ===")
    print(f"Average GDP per capita: {average_gdp:,.2f} USD")
    print(f"Highest life expectancy: {max_life} years ({max_country})")
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


def main():
    print("Welcome to 'The Wealth of Nations' project!")

    filepath = "data/demo_countries.csv"
    data = load_demo_data(filepath)

    if not data:
        print("No data loaded. Exiting program.")
        return

    print("Demo data loaded successfully.")
    print_countries(data)        # new helper function
    analyze_demo_data(data)      # analysis as before



if __name__ == "__main__":
    main()
