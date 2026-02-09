# <output_database_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
#     "adbc-driver-sqlite",
#     "sqlalchemy",
#     "pandas",
#     "pyarrow",
# ]
# ///
import polars as pl
import os

# Create a sample summary dataframe
df = pl.DataFrame({
    'species': ['Adelie', 'Chinstrap', 'Gentoo'],
    'avg_mass_g': [3701, 3733, 5076]
})

# 1. Database Connection URI
db_path = "penguins_pl.db"
uri = f"sqlite:///{db_path}"

# 2. Write to Database
print(f"--- Exporting to {db_path} ---")
df.write_database(
    table_name="species_summary",
    connection=uri,
    if_table_exists="replace"
)
print(f"✅ Successfully wrote {len(df)} rows to 'species_summary' table.")

# Clean up
if os.path.exists(db_path):
    os.remove(db_path)
# </output_database_polars>
