import requests
import pandas as pd
from typing import Optional
from src.grouping import GroupClassifier


# --- CONSTANT ---
GDP_INDICATOR = "NY.GDP.PCAP.CD"


# --- 1. CSV LOADING (Kept from your original file for fallback) ---
def load_gdp_per_capita_from_csv(filepath):
    """
    Load GDP per capita data from the World Bank SDMX-style CSV.
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

    return df[["region_code", "region_name", "year", "gdp_per_capita"]]


# --- 2. API FETCHING (Your new function using requests) ---
def fetch_gdp_per_capita_from_api(
    start_year: int, 
    end_year: int,
    indicator: str = GDP_INDICATOR
) -> Optional[pd.DataFrame]:
    """
    Fetch GDP per capita data (NY.GDP.PCAP.CD) from the World Bank API
    for all regions over a specified time range.
    """
    # 1. Construct the API URL
    url = (
        f"http://api.worldbank.org/v2/country/all/indicator/{indicator}"
        f"?date={start_year}:{end_year}&format=json&per_page=10000"
    )

    print(f"Fetching data from World Bank API for {indicator}...")
    
    # 2. Make the GET request and handle errors
    try:
        response = requests.get(url)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from World Bank API: {e}")
        return None

    # 3. Process the JSON response
    data = response.json()
    if len(data) < 2 or data[1] is None:
        print("API returned no data or an unexpected format.")
        return None

    records = data[1]

    # 4. Flatten the JSON structure for the DataFrame
    processed_records = []
    for record in records:
        if record is not None and record.get("value") is not None:
            processed_records.append({
                "region_code": record.get("countryiso3code"),
                "region_name": record["country"]["value"],
                "year": int(record["date"]),
                "gdp_per_capita": record["value"] 
            })

    # 5. Convert to DataFrame and clean
    df = pd.DataFrame(processed_records)
    df["gdp_per_capita"] = pd.to_numeric(df["gdp_per_capita"], errors="coerce")
    df = df.dropna(subset=["gdp_per_capita"]) 
    
    return df[['region_code', 'region_name', 'year', 'gdp_per_capita']]


# --- 3. UNIFIED LOADING & FILTERING (Final function for analysis) ---
def load_gdp_data(use_api: bool = True) -> Optional[pd.DataFrame]:
    """
    Loads and cleans World Bank GDP data, either from API or local CSV.
    Filters out aggregate regions using the GroupClassifier.
    """
    
    # 1. DATA SOURCE: Select API or CSV
    if use_api:
        df = fetch_gdp_per_capita_from_api(start_year=2000, end_year=2020)
    else:
        df = load_gdp_per_capita_from_csv("data/worldbank_gdp_per_capita.csv")
    
    if df is None or df.empty:
        print("Data loading failed.")
        return None

    # --- CRITICAL FILTERING STEPS ---
    
    # 2. Classify: Use the GroupClassifier to identify aggregates
    classifier = GroupClassifier()
    df["group_type"] = df["region_name"].apply(classifier.classify) 

    # 3. Filter: Keep only the individual countries (tagged as 'other' by the classifier)
    df = df[df["group_type"] == "other"].copy()

    # 4. Rename: Change the 'other' tag to 'country' for clarity
    df["group_type"] = "country"
    
    # -------------------------------

    return df