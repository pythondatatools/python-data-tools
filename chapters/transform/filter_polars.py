# <transform_filter_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
#     "fsspec",
#     "requests",
# ]
# ///
import polars as pl
import io

# ---------------------------------------------------------
# Load Dataset (Palmer Penguins)
# ---------------------------------------------------------
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

try:
    # Polars can read from URL directly
    df = pl.read_csv(URL)
except Exception:
    print("Warning: Failed to load data from URL. Mocking data.")
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
    df = pl.read_csv(io.StringIO(data))

print(f"Loaded {len(df)} rows.")

# ---------------------------------------------------------
# 1. Basic Filtering (pl.col expression)
# ---------------------------------------------------------
# Select only 'Adelie' penguins
# In Polars, .filter() is the primary method
adelie_df = df.filter(pl.col("species") == "Adelie")
print("\n--- Filter: Species == 'Adelie' ---")
print(adelie_df.head(3))

# ---------------------------------------------------------
# 2. Multiple Conditions
# ---------------------------------------------------------
# Select 'Adelie' penguins from 'Torgersen' island
# Use & for AND, | for OR. Parentheses are required!
torgersen_adelie = df.filter(
    (pl.col("species") == "Adelie") & 
    (pl.col("island") == "Torgersen")
)
print("\n--- Filter: Species == 'Adelie' AND Island == 'Torgersen' ---")
print(torgersen_adelie.head(3))

# ---------------------------------------------------------
# 3. Numeric Comparison
# ---------------------------------------------------------
# Select penguins with bill length > 45mm
long_bills = df.filter(pl.col("bill_length_mm") > 45)
print("\n--- Filter: bill_length_mm > 45 ---")
print(long_bills.head(3))

# ---------------------------------------------------------
# 4. String Matching
# ---------------------------------------------------------
# Select penguins where island starts with 'B' (Biscoe)
biscoe_df = df.filter(pl.col("island").str.starts_with("B"))
print("\n--- Filter: Island starts with 'B' ---")
print(biscoe_df.head(3))

# ---------------------------------------------------------
# 5. Null Handling
# ---------------------------------------------------------
# Drop rows where 'sex' is null
clean_df = df.drop_nulls(subset=["sex"])
print(f"\n--- Drop Nulls in 'sex' ---")
print(f"Original: {len(df)}, Cleaned: {len(clean_df)}")
# </transform_filter_polars>
