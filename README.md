🌍 The Wealth of Nations

A Modular Python Application for Analyzing Global Prosperity

This project analyzes GDP per capita across countries over time using data from the World Bank.
It demonstrates a complete Python data-processing workflow, including:

- Pure Python CSV handling
- Pandas and NumPy data analysis
- Object-Oriented Programming
- Matplotlib visualisations
- Clean modular architecture
- Streamlit dashboard

The main question explored is:

How has global prosperity evolved across countries from 2000 to 2020?

Project Structure

wealth-of-nations/
├── data/
│   ├── demo_countries.csv
│   └── global_gdp_trend.png    <-- Visualization Output
│
├── src/                        <-- Source Code
│   ├── analysis.py             # Statistical analysis (NumPy, Pandas)
│   ├── grouping.py             # Region classification logic
│   ├── load_wb_data.py         # API/CSV loading and critical filtering
│   ├── models.py               # GDPRegion Class (OOP) 
│   └── visualization.py        # Matplotlib plotting logic 
│
├── app.py                      # Streamlit Dashboard 
├── requirements.txt             
└── README.md

Features
1. Pure Python data analysis (demo_data.py)

A small dataset is processed without pandas:

- Manual CSV reading using .readlines()
- Dictionaries and loops
- Average GDP per capita
- Highest life expectancy
- Countries above average GDP

2. World Bank Data Loader (load_wb_data.py)

Fetches GDP per capita (current US$) for 2000–2020 using the World Bank API, with automatic CSV fallback.

Includes:

- Data cleaning
- Type conversion
- Removal of aggregate pseudo-countries (e.g., High Income, Euro Area)
- Integration with region classifier

3. Region classification with OOP (grouping.py)

Contains the GroupClassifier class that assigns:

- geographic regions
- income groups
- demographic groups
- other (countries)

Used by the loader for clean modular design.

4. GDPRegion class (models.py)

Represents a single country–year observation with:

- Attributes (country, year, GDP)
- Utility methods (e.g., is_high_income())

Used in the main script to demonstrate OOP concepts.

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
- World Bank loading
- Cleaning, filtering and classification
- Statistical computations
- Saving plots
- OOP demonstration with GDPRegion objects

8. Interactive Dashboard (app.py)

A Streamlit web app featuring:

- Caching (@st.cache_data)
- Country selector
- Trend visualisations
- Summary metrics

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

World Bank — GDP per capita (current US$)
Data fetched via API using requests (2000–2020).
A local CSV is used as a fallback when API calls fail.
All cleaning, filtering and region assignments are handled internally.

Skills Demonstrated:

- Python fundamentals
- Data structures
- File I/O
- Object-Oriented Programming
- pandas & NumPy
- Data visualization
- Modular architecture
- Streamlit (interactive UI)


Methodology Notes:
The project incorporated AI-augmented coding practices using ChatGPT as a pair-programming assistant. AI support was used to prototype functions, refactor code for modularity, streamline the Streamlit interface, and validate the mathematical consistency of the analyses. The workflow followed a human-in-the-loop approach: AI provided suggestions, which were then critically assessed, adapted, and manually implemented. This enhanced productivity while ensuring that the analytical logic and final implementations remained fully human-validated.

Author:

Stela Mile
MSc Data Science for Economics & Health
Università degli Studi di Milano