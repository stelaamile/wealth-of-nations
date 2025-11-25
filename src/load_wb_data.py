import pandas as pd


def load_gdp_per_capita_from_csv(filepath):
    """
    Load GDP per capita data from the World Bank SDMX-style CSV.

    Returns a DataFrame with columns:
    - region_code
    - region_name
    - year
    - gdp_per_capita
    - group_type   (geographic / income_group / demographic_group / other)
    """

    # 1. Read the CSV file
    df = pd.read_csv(filepath)

    # 2. Keep only the columns we care about
    df = df[["REF_AREA", "REF_AREA_LABEL", "TIME_PERIOD", "OBS_VALUE"]]

    # 3. Rename them to simpler names
    df = df.rename(
        columns={
            "REF_AREA": "region_code",
            "REF_AREA_LABEL": "region_name",
            "TIME_PERIOD": "year",
            "OBS_VALUE": "gdp_per_capita",
        }
    )

    # 4. Convert year to integer
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df = df.dropna(subset=["year"])
    df["year"] = df["year"].astype(int)

    # 5. Convert GDP per capita to float and drop missing values
    df["gdp_per_capita"] = pd.to_numeric(df["gdp_per_capita"], errors="coerce")
    df = df.dropna(subset=["gdp_per_capita"])

    # 6. Classify each REF_AREA_LABEL into a group type
    geographic_regions = {
        "Africa Eastern and Southern",
        "Africa Western and Central",
        "East Asia & Pacific",
        "East Asia & Pacific (excluding high income)",
        "Europe & Central Asia",
        "Latin America & Caribbean",
        "Middle East & North Africa",
        "North America",
        "South Asia",
        "Sub-Saharan Africa",
        "Caribbean small states",
        "Euro area",
        "European Union",
    }

    income_groups = {
        "High income",
        "Upper middle income",
        "Lower middle income",
        "Low income",
    }

    demographic_groups = {
        "Early-demographic dividend",
        "Late-demographic dividend",
        "Pre-demographic dividend",
        "Post-demographic dividend",
    }

    def classify_group(name: str) -> str:
        if name in geographic_regions:
            return "geographic"
        if name in income_groups:
            return "income_group"
        if name in demographic_groups:
            return "demographic_group"
        return "other"

    df["group_type"] = df["region_name"].apply(classify_group)

    return df
