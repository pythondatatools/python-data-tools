# <transform_filter_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
#     "pandas",
# ]
# ///
import duckdb
import pandas as pd
import io

# ---------------------------------------------------------
# Load Dataset (Palmer Penguins)
# ---------------------------------------------------------
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
TABLE_NAME = "penguins"

try:
    # DuckDB handles HTTPS if httpfs is installed/loaded (auto-loaded in modern versions)
    # We create a view or table to query against easily
    duckdb.sql(f"CREATE OR REPLACE TABLE {TABLE_NAME} AS SELECT * FROM '{URL}'")
    print(f"Loaded data from {URL} into DuckDB table '{TABLE_NAME}'")
except Exception:
    print("Warning: Failed to load data from URL. Mocking data via Pandas.")
    data = """species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,Male
Adelie,Torgersen,39.5,17.4,186,3800,Female
Adelie,Torgersen,40.3,18.0,195,3250,Female
Adelie,Torgersen,36.7,19.3,193,3450,Female
Adelie,Torgersen,39.3,20.6,190,3650,Male
Chinstrap,Dream,46.5,17.9,192,3500,Female
Chinstrap,Dream,50.0,19.5,196,3900,Male
Gentoo,Biscoe,46.1,13.2,211,4500,Female
Gentoo,Biscoe,50.0,16.3,230,5700,Male
"""
    # Create a Pandas DataFrame
    pandas_df = pd.read_csv(io.StringIO(data))
    # DuckDB can query Pandas DataFrames directly!
    duckdb.sql(f"CREATE OR REPLACE TABLE {TABLE_NAME} AS SELECT * FROM pandas_df")

# ---------------------------------------------------------
# 1. Basic Filtering (SQL WHERE)
# ---------------------------------------------------------
# Select only 'Adelie' penguins
print("\n--- Filter: Species = 'Adelie' ---")
duckdb.sql(f"SELECT * FROM {TABLE_NAME} WHERE species = 'Adelie' LIMIT 3").show()

# ---------------------------------------------------------
# 2. Multiple Conditions (AND/OR)
# ---------------------------------------------------------
# Select 'Adelie' penguins from 'Torgersen' island
print("\n--- Filter: Species = 'Adelie' AND Island = 'Torgersen' ---")
duckdb.sql(f"""
    SELECT * FROM {TABLE_NAME} 
    WHERE species = 'Adelie' AND island = 'Torgersen' 
    LIMIT 3
""").show()

# ---------------------------------------------------------
# 3. Numeric Comparison
# ---------------------------------------------------------
# Select penguins with bill length > 45mm
print("\n--- Filter: bill_length_mm > 45 ---")
duckdb.sql(f"SELECT * FROM {TABLE_NAME} WHERE bill_length_mm > 45 LIMIT 3").show()

# ---------------------------------------------------------
# 4. String Matching (LIKE/ILIKE)
# ---------------------------------------------------------
# Select penguins where island starts with 'B' (Biscoe)
# '%' is the wildcard in SQL
print("\n--- Filter: Island LIKE 'B%' ---")
duckdb.sql(f"SELECT * FROM {TABLE_NAME} WHERE island LIKE 'B%' LIMIT 3").show()

# ---------------------------------------------------------
# 5. Null Handling (IS NOT NULL)
# ---------------------------------------------------------
# Drop rows where 'sex' is null
print(f"\n--- Drop Nulls in 'sex' ---")
result = duckdb.sql(f"SELECT * FROM {TABLE_NAME} WHERE sex IS NOT NULL")
print(f"Original: {duckdb.sql(f'SELECT count(*) FROM {TABLE_NAME}').fetchone()[0]}")
print(f"Cleaned: {result.count('*').fetchone()[0]}")
# </transform_filter_duckdb>
