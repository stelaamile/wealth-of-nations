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


def main():
    print("Welcome to 'The Wealth of Nations' project!")

    filepath = "data/demo_countries.csv"
    data = load_demo_data(filepath)

    print("Demo data loaded:")
    print(data)


if __name__ == "__main__":
    main()
