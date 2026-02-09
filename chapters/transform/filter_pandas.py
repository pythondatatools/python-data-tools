# <transform_filter_pandas>
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
    print("Warning: Failed to load data from URL. Mocking data.")
    # Mock data for demonstration
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
    df = pd.read_csv(io.StringIO(data))

print(f"Loaded {len(df)} rows.")

# ---------------------------------------------------------
# 1. Basic Filtering (Boolean Indexing)
# ---------------------------------------------------------
# Select only 'Adelie' penguins
adelie_df = df[df['species'] == 'Adelie']
print("\n--- Filter: Species == 'Adelie' ---")
print(adelie_df.head(3))

# ---------------------------------------------------------
# 2. Multiple Conditions
# ---------------------------------------------------------
# Select 'Adelie' penguins from 'Torgersen' island
# Note: Parentheses are mandatory for multiple conditions in Pandas!
condition = (df['species'] == 'Adelie') & (df['island'] == 'Torgersen')
torgersen_adelie = df[condition]
print("\n--- Filter: Species == 'Adelie' AND Island == 'Torgersen' ---")
print(torgersen_adelie.head(3))

# ---------------------------------------------------------
# 3. Using .query() (String Syntax)
# ---------------------------------------------------------
# Select penguins with bill length > 45mm
long_bills = df.query("bill_length_mm > 45")
print("\n--- Filter: bill_length_mm > 45 (using .query()) ---")
print(long_bills.head(3))

# ---------------------------------------------------------
# 4. String Matching
# ---------------------------------------------------------
# Select penguins where island starts with 'B' (Biscoe)
biscoe_df = df[df['island'].str.startswith('B')]
print("\n--- Filter: Island starts with 'B' ---")
print(biscoe_df.head(3))

# ---------------------------------------------------------
# 5. Null Handling
# ---------------------------------------------------------
# Drop rows where 'sex' is missing
clean_df = df.dropna(subset=['sex'])
print(f"\n--- Drop Nulls in 'sex' ---")
print(f"Original: {len(df)}, Cleaned: {len(clean_df)}")
# </transform_filter_pandas>
