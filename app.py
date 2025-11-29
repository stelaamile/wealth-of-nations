import streamlit as st
import pandas as pd

# CRITICAL: Import the unified loader (load_gdp_data)
# Note: You can remove the unused import 'load_gdp_per_capita_from_csv'
from src.load_wb_data import load_gdp_data 

from src.analysis import (
    compute_global_yearly_average,
    summarize_global_trend,
    compute_region_vs_world,
    compute_rich_poor_gap,
)


@st.cache_data # <-- FIX 1: Add the caching decorator
def load_worldbank_data() -> pd.DataFrame:
    """
    Load and cache the World Bank GDP per capita dataset, 
    using the API loader which includes the country-level filter.
    """
    # FIX 2: Use the unified load_gdp_data function
    # It attempts API first, then falls back to CSV, and includes the country filter.
    df = load_gdp_data(use_api=True) 
    
    # Handle failure (Streamlit best practice)
    if df is None:
        st.error("Could not load data from API or local file. Check console for details.")
        return pd.DataFrame()
        
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

    # ----------------------------
    # DATA PREVIEW SECTION
    # ----------------------------
    st.subheader("Data preview")

    # We now work only with country-level data
    preview_label = "Countries"
    preview_type = "country"

    st.write(f"Showing data for: **{preview_label}**")

    # Filter once by group_type (redundant but explicit)
    filtered_df = df[df["group_type"] == preview_type]


    # Table: drop group_type column (redundant)
    preview_df = (
        filtered_df.loc[:, ["region_code", "region_name", "year", "gdp_per_capita"]]
        .reset_index(drop=True)
    )

    st.dataframe(preview_df.head(50), use_container_width=True)

    st.caption(
        f"Showing {min(50, len(filtered_df)):,} of {len(filtered_df):,} rows "
        f"for group type: **{preview_label}**"
    )

     # ----------------------------
    # FOCUS ON SINGLE COUNTRY
    # ----------------------------
    st.subheader("Focus on a single country")

    if filtered_df.empty:
        st.info("No data available.")
    else:
        # 👉 ALL countries available
        country_options = sorted(filtered_df["region_name"].unique())

        selected_country = st.selectbox(
            "Select a country to analyze:",
            country_options,
        )

        # Show all rows for this country (no .head(50) here!)
        country_detail = (
            filtered_df[filtered_df["region_name"] == selected_country]
            .loc[:, ["year", "gdp_per_capita"]]
            .sort_values("year")
            .reset_index(drop=True)
        )

        st.write(f"GDP per capita over time – **{selected_country}**")
        st.dataframe(country_detail, use_container_width=True)

        # Country vs world chart synced with selection
        country_vs_world = compute_region_vs_world(df, selected_country)
        country_vs_world = country_vs_world.set_index("year")
        st.subheader(f"{selected_country} vs World – GDP per Capita")
        st.line_chart(country_vs_world, height=350)

    # ----------------------------
    # GLOBAL OVERVIEW (ALL DATA)
    # ----------------------------
    st.header("🌐 Global Prosperity Overview")

    summary_global = summarize_global_trend(df)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label=f"GDP per capita in {summary_global['first_year']}",
        value=f"${summary_global['first_value']:,.0f}",
    )

    col2.metric(
        label=f"GDP per capita in {summary_global['last_year']}",
        value=f"${summary_global['last_value']:,.0f}",
    )

    col3.metric(
        label="Growth since 1960",
        value=f"{summary_global['growth_pct']:.1f}%",
    )

    st.subheader("Global Average GDP per Capita Over Time")

    yearly_avg_global = compute_global_yearly_average(df)
    st.line_chart(yearly_avg_global, height=350)

    # ----------------------------
    # OVERVIEW FOR SELECTED GROUP TYPE
    # ----------------------------
    nice_name = preview_label  # already pretty
    st.header(f"📊 Prosperity Overview – {nice_name}")

    if filtered_df.empty:
        st.info("No data available for this group type.")
    else:
        summary_group = summarize_global_trend(filtered_df)

        c1, c2, c3 = st.columns(3)
        c1.metric(
            label=f"GDP per capita in {summary_group['first_year']}",
            value=f"${summary_group['first_value']:,.0f}",
        )
        c2.metric(
            label=f"GDP per capita in {summary_group['last_year']}",
            value=f"${summary_group['last_value']:,.0f}",
        )
        c3.metric(
            label=f"Growth since {summary_group['first_year']}",
            value=f"{summary_group['growth_pct']:.1f}%",
        )

        st.subheader(f"{nice_name}: Average GDP per Capita Over Time")

        yearly_avg_group = compute_global_yearly_average(filtered_df)
        st.line_chart(yearly_avg_group, height=350)


if __name__ == "__main__":
    main()
