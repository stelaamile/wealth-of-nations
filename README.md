# wealth-of-nations
This project analyzes GDP per capita for a selected set of countries using data from the World Bank. It demonstrates key skills from the course, including a clean project structure, modular code, data loading, and reproducible environments using virtual environments.

The project loads a local World Bank dataset (worldbank_gdp_per_capita.csv), cleans it, and computes summary statistics for countries listed in demo_countries.csv.

Project Structure

project_root/
├── data/
│ ├── demo_countries.csv
│ └── worldbank_gdp_per_capita.csv
│
├── src/
│ ├── load_wb_data.py
│ └── analyze_gdp.py
│
├── venv/
│
├── .gitignore
├── requirements.txt
└── README.md

Data Sources

World Bank — GDP per capita (current US$)
Local file: data/worldbank_gdp_per_capita.csv
This file includes a metadata header row, which is cleaned automatically by load_wb_data.py.

Demo countries
Local file: data/demo_countries.csv
Contains ISO-3 country codes used to filter the GDP dataset.

Installation

Clone the repository

git clone https://github.com/
<your-username>/<your-repo>.git
cd <your-repo>

Create and activate the virtual environment

python3 -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Running the Project

Run the GDP analysis script:

python -m src.analyze_gdp

This will load and clean the World Bank GDP CSV, filter the data to the demo countries, compute summary statistics, and print the results to the terminal.

Dependencies

Listed in requirements.txt:

pandas

Git Usage

This project follows recommended Git practices:

.gitignore excludes unnecessary files such as venv/, pycache/ and .DS_Store

commits are frequent, small, and have clear messages

the README documents project purpose, installation, and usage

Example commit messages:

feat: add World Bank GDP loader
feat: implement GDP analysis script
fix: clean metadata row from CSV
docs: update README with run instructions
