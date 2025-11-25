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
    
    # Mapping from internal labels to pretty labels
    pretty_labels = {
        "geographic": "Geographic",
        "income_group": "Income Group",
        "demographic_group": "Demographic Group",
        "other": "Other"
    }

    # Reverse mapping for selection
    inv_map = {v: k for k, v in pretty_labels.items()}

    preview_label = st.selectbox(
        "Group type:",
        list(pretty_labels.values()),  # pretty names
        index=0,
    )

    preview_type = inv_map[preview_label]  # convert pretty → internal


    # Filter once by selected group_type
    filtered_df = df[df["group_type"] == preview_type]

    # Table: drop group_type column (redundant)
    preview_df = (
        filtered_df.loc[:, ["region_code", "region_name", "year", "gdp_per_capita"]]
        .reset_index(drop=True)
    )

    st.dataframe(preview_df.head(50), use_container_width=True)

    st.caption(
        f"Showing {min(50, len(filtered_df)):,} of {len(filtered_df):,} rows "
        f"for group type: **{preview_type}**"
    )

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
    nice_name = preview_type.replace("_", " ").title()
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
