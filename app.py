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

    # ----------------------------
    # DATA PREVIEW SECTION
    # ----------------------------
    st.subheader("Data preview")

    st.write("Select which group type you want to preview:")

    preview_type = st.selectbox(
        "Group type:",
        ["geographic", "income_group", "demographic_group", "other"],
        index=0,
    )

    preview_df = (
        df[df["group_type"] == preview_type]
        .loc[:, ["region_code", "region_name", "year", "gdp_per_capita", "group_type"]]
        .reset_index(drop=True)
    )

    st.dataframe(preview_df.head(50), use_container_width=True)

    st.caption(
        f"Showing {min(50, len(preview_df)):,} of {len(preview_df):,} rows "
        f"for group type: **{preview_type}**"
    )

    # ----------------------------
    # GLOBAL OVERVIEW SECTION
    # ----------------------------
    st.header("🌐 Global Prosperity Overview")

    # Compute summary stats
    summary = summarize_global_trend(df)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label=f"GDP per capita in {summary['first_year']}",
        value=f"${summary['first_value']:,.0f}",
    )

    col2.metric(
        label=f"GDP per capita in {summary['last_year']}",
        value=f"${summary['last_value']:,.0f}",
    )

    col3.metric(
        label="Growth since 1960",
        value=f"{summary['growth_pct']:.1f}%",
    )

    # Line plot — global average over time
    st.subheader("Global Average GDP per Capita Over Time")

    yearly_avg = compute_global_yearly_average(df)

    st.line_chart(
        yearly_avg,
        height=350
    )


if __name__ == "__main__":
    main()
