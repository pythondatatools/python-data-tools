# <transform_aggregate_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
# ]
# ///
import pandas as pd
import io

# ---------------------------------------------------------
# Load Dataset (Palmer Penguins)
# ---------------------------------------------------------
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

try:
    df = pd.read_csv(URL)
except Exception:
    # Mock data fallback
    data = """species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,Male
Adelie,Torgersen,39.5,17.4,186,3800,Female
Chinstrap,Dream,46.5,17.9,192,3500,Female
Gentoo,Biscoe,46.1,13.2,211,4500,Female
Gentoo,Biscoe,50.0,16.3,230,5700,Male
"""
    df = pd.read_csv(io.StringIO(data))

print(f"Loaded {len(df)} rows.")

# ---------------------------------------------------------
# 1. Basic Aggregation (Mean Body Mass by Species)
# ---------------------------------------------------------
# Simple groupby + mean
avg_mass = df.groupby('species')['body_mass_g'].mean().reset_index()
print("\n--- Average Body Mass by Species ---")
print(avg_mass)

# ---------------------------------------------------------
# 2. Multiple Aggregations (.agg)
# ---------------------------------------------------------
# Get count, mean, min, and max in one go
stats = df.groupby('species')['body_mass_g'].agg(['count', 'mean', 'min', 'max'])
print("\n--- Summary Statistics by Species ---")
print(stats)

# ---------------------------------------------------------
# 3. Grouping by Multiple Columns
# ---------------------------------------------------------
# Average bill length by species and island
geo_stats = df.groupby(['species', 'island'])['bill_length_mm'].mean().reset_index()
print("\n--- Average Bill Length (Species + Island) ---")
print(geo_stats.head(5))

# ---------------------------------------------------------
# 4. Named Aggregation (Pandas 0.25+)
# ---------------------------------------------------------
# More descriptive column names in final result
named_agg = df.groupby('species').agg(
    total_penguins=('species', 'count'),
    avg_weight_g=('body_mass_g', 'mean'),
    max_bill_mm=('bill_length_mm', 'max')
)
print("\n--- Named Aggregations ---")
print(named_agg)
# </transform_aggregate_pandas>
