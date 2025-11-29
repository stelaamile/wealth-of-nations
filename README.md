🌍 The Wealth of Nations

A Modular Python Application for Analyzing Global Prosperity

This project analyzes GDP per capita across countries over time using data from the World Bank.
It demonstrates a complete Python data-processing workflow, including:

- Pure Python CSV handling
- Pandas and NumPy data analysis
- Object-Oriented Programming
- Matplotlib visualisations
- Clean modular architecture
- Streamlit dashboard (optional bonus)

The main question explored is:

How has global prosperity evolved across countries from 1960 to today?

Project Structure

wealth-of-nations/
├── data/
│   ├── demo_countries.csv
│   ├── worldbank_gdp_per_capita.csv
│   └── global_gdp_trend.png
│
├── src/
│   ├── analysis.py
│   ├── demo_data.py
│   ├── grouping.py
│   ├── load_wb_data.py
│   ├── main.py
│   ├── models.py
│   └── visualization.py
│
├── app.py
├── requirements.txt
└── README.md

Features
1. Pure Python data analysis (demo_data.py)

A small dataset is parsed without pandas:
- Manual CSV reading using .readlines()
- Dictionaries and loops
- Average GDP per capita
- Highest life expectancy
- Countries above average GDP

2. World Bank Data Loader (load_wb_data.py)

Uses the **requests** library to fetch data from the World Bank API for 2000-2020 (with CSV fallback). The data is cleaned and filtered to **remove aggregate regions** (e.g., 'World', 'High Income') using the GroupClassifier, ensuring only country-level data remains.

3. Region classification with OOP (grouping.py)

Contains the GroupClassifier class that assigns:
- geographic regions
- income groups
- demographic groups
- other (countries)

Used by the loader for clean modular design.

4. GDPRegion class (models.py)

Represents a single country-year observation with attributes and a method:
- is_high_income()

Demonstrated in main.py.

5. Analytical functions (analysis.py)

Includes:
- Global yearly average GDP
- Growth summary
- Country vs world comparison
- Richest–poorest country gap

6. Visualization (visualization.py)

Creates and saves:

- global_gdp_trend.png

7. Main script (src/main.py)

Runs the full pipeline:
- Pure Python demo analysis
- World Bank loading + cleaning
- Stats and trends
- Saving plots
- OOP demonstration with GDPRegion objects

8. Streamlit Dashboard (app.py) An interactive interface featuring caching (using **@st.cache_data**) for fast performance, live metrics, country selector, and trends.

Installation:
git clone <your-repo-url>
cd wealth-of-nations
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

How to Run:
1. Run the full analysis (CLI)
python -m src.main

2. Run the dashboard (optional)
streamlit run app.py

Data Source:

World Bank — GDP per capita (current US$), fetched via **API** (requests) from 2000-2020. Local CSV data is used as a fallback. Data is cleaned and filtered inside load_wb_data.py.

Skills Demonstrated:

- Python fundamentals
- Data structures
- File I/O
- Object-Oriented Programming
- pandas & NumPy
- Data visualization
- Modular architecture
- Streamlit (interactive UI)

Author:

Stela Mile
MSc Data Science for Economics & Health
Università degli Studi di Milano