# <load_csv_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
# ]
# ///
import duckdb
import pathlib

# Self-healing: Generate data if missing for portability
path = pathlib.Path("data.csv")
if not path.exists():
    import pandas as pd
    pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "city": ["NY", "SF", "LA"]
    }).to_csv(path, index=False)

# Query CSV directly
result = duckdb.sql(f"SELECT * FROM '{path}'")
print(f"DuckDB found {len(result.fetchall())} rows:")
duckdb.sql(f"SELECT * FROM '{path}'").show()
# </load_csv_duckdb>
