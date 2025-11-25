This project analyzes GDP per capita for a selected set of countries using data from the World Bank.
It demonstrates key skills from the course:

clean project structure

modular code

data loading from external sources

data cleaning and manipulation with pandas

scientific computing with NumPy

visualisation with matplotlib

reproducible environments with virtual environments

The project loads a local World Bank dataset (worldbank_gdp_per_capita.csv), cleans it, and computes summary statistics. It also includes a small demo dataset (demo_countries.csv) loaded using basic Python to illustrate manual CSV handling.

Project Structure
project_root/
├── data/
│   ├── demo_countries.csv
│   ├── worldbank_gdp_per_capita.csv
│   └── global_gdp_trend.png        # generated plot
│
├── src/
│   ├── __init__.py
│   ├── load_wb_data.py
│   └── main.py
│
├── venv/
│
├── .gitignore
├── requirements.txt
└── README.md

Data Sources

World Bank — GDP per capita (current US$)
Local file: data/worldbank_gdp_per_capita.csv
The file includes metadata columns, which are cleaned automatically by load_wb_data.py.

Demo countries dataset
Local file: data/demo_countries.csv
Used to demonstrate basic Python CSV parsing (no pandas).

Installation

Clone the repository:

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>


Create and activate the virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

Running the Project

Run the main script:

python -m src.main


This will:

load and display the demo dataset

compute simple statistics using pure Python

load and clean the World Bank GDP dataset using pandas

compute global numerical statistics using NumPy

display the top 5 richest regions in the latest year

generate a plot of the global average GDP per capita over time and save it as:

data/global_gdp_trend.png

Dependencies

Listed in requirements.txt:

pandas
numpy
matplotlib

Git Usage

This project follows recommended Git practices:

.gitignore excludes unnecessary files such as venv/, __pycache__/, and .DS_Store

commits are small, frequent, and have descriptive messages

README provides clear installation and usage instructions

Example commit messages:

feat: add World Bank GDP loader
feat: integrate GDP statistics and analysis
feat: add global GDP trend plot using matplotlib
fix: clean metadata row from World Bank dataset
docs: update README with project usage and plot description