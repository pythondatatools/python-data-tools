# <transform_aggregate_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
# ]
# ///
import polars as pl
import io

# ---------------------------------------------------------
# Load Dataset (Palmer Penguins)
# ---------------------------------------------------------
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

try:
    df = pl.read_csv(URL)
except Exception:
    data = """species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,Male
Adelie,Torgersen,39.5,17.4,186,3800,Female
Chinstrap,Dream,46.5,17.9,192,3500,Female
Gentoo,Biscoe,46.1,13.2,211,4500,Female
Gentoo,Biscoe,50.0,16.3,230,5700,Male
"""
    df = pl.read_csv(io.StringIO(data))

print(f"Loaded {len(df)} rows.")

# ---------------------------------------------------------
# 1. Basic Aggregation (Mean Mass by Species)
# ---------------------------------------------------------
# In Polars, group_by + agg is the standard flow
avg_mass = df.group_by("species").agg(
    pl.col("body_mass_g").mean().alias("avg_mass")
)
print("\n--- Average Body Mass by Species ---")
print(avg_mass)

# ---------------------------------------------------------
# 2. Multiple Aggregations
# ---------------------------------------------------------
# Polars expressions allow many aggregates in one list
stats = df.group_by("species").agg([
    pl.len().alias("count"),
    pl.col("body_mass_g").mean().alias("mean"),
    pl.col("body_mass_g").min().alias("min"),
    pl.col("body_mass_g").max().alias("max"),
])
print("\n--- Summary Statistics by Species ---")
print(stats)

# ---------------------------------------------------------
# 3. Grouping by Multiple Columns
# ---------------------------------------------------------
geo_stats = df.group_by(["species", "island"]).agg(
    pl.col("bill_length_mm").mean().alias("avg_bill")
).sort("avg_bill", descending=True)

print("\n--- Average Bill Length (Species + Island) ---")
print(geo_stats.head(5))

# ---------------------------------------------------------
# 4. Expressions within Aggregation
# ---------------------------------------------------------
# Calculate the spread (max - min) while grouping
complex_agg = df.group_by("species").agg(
    spread=(pl.col("body_mass_g").max() - pl.col("body_mass_g").min())
)
print("\n--- Body Mass Spread by Species ---")
print(complex_agg)
# </transform_aggregate_polars>
