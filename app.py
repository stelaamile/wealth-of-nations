import streamlit as st
import pandas as pd

from src.load_wb_data import load_gdp_per_capita_from_csv
from src.analysis import (
    compute_global_yearly_average,
    summarize_global_trend,
    compute_region_vs_world,
    compute_rich_poor_gap,
)


@st.cache_data
def load_worldbank_data() -> pd.DataFrame:
    """
    Load and cache the World Bank GDP per capita dataset.

    Returns:
        pd.DataFrame: Cleaned GDP per capita data.
    """
    filepath = "data/worldbank_gdp_per_capita.csv"
    df = load_gdp_per_capita_from_csv(filepath)
    return df


def main():
    """Streamlit entry point for the Global Prosperity Explorer."""
    st.set_page_config(
        page_title="Global Prosperity Explorer",
        page_icon="🌍",
        layout="wide",
    )

    st.title("🌍 Global Prosperity Explorer")
    st.write(
        "Interactive dashboard built with World Bank GDP per capita data. "
        "This is the skeleton version – we will add more sections next."
    )

    # Load data (cached)
    df = load_worldbank_data()

    st.subheader("Data preview")
    st.write("First 5 rows of the cleaned World Bank dataset:")
    st.dataframe(df.head())

    st.write(f"Number of rows: {len(df)}")
    st.write(f"Columns: {list(df.columns)}")


if __name__ == "__main__":
    main()
