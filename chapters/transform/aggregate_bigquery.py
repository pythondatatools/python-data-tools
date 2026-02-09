# <transform_aggregate_bigquery>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-cloud-bigquery",
#     "pandas",
# ]
# ///
import pandas as pd
from unittest.mock import MagicMock

# ---------------------------------------------------------
# Mocking BigQuery Client for Portability
# ---------------------------------------------------------
class MockBQClient:
    def __init__(self):
        print("--- BigQuery Client Initialized (Mock) ---")
    
    def query(self, sql):
        print(f"\nExecuting SQL:\n{sql}")
        
        # Determine which result to return based on SQL content
        if "AVG(body_mass_g)" in sql and "GROUP BY species" in sql and "COUNT(*)" not in sql:
            return MagicMock(to_dataframe=lambda: pd.DataFrame({
                'species': ['Adelie', 'Chinstrap', 'Gentoo'],
                'avg_mass': [3700.6, 3733.1, 5076.0]
            }))
        elif "COUNT(*)" in sql and "MIN(body_mass_g)" in sql:
            return MagicMock(to_dataframe=lambda: pd.DataFrame({
                'species': ['Adelie', 'Chinstrap', 'Gentoo'],
                'count': [152, 68, 124],
                'mean': [3700.6, 3733.1, 5076.0],
                'min': [2850.0, 2700.0, 3950.0],
                'max': [4775.0, 4800.0, 6300.0]
            }))
        elif "island" in sql:
            return MagicMock(to_dataframe=lambda: pd.DataFrame({
                'species': ['Gentoo', 'Gentoo', 'Adelie'],
                'island': ['Biscoe', 'Dream', 'Torgersen'],
                'avg_bill': [47.5, 46.2, 38.8]
            }))
        else:
            return MagicMock(to_dataframe=lambda: pd.DataFrame({'status': ['OK']}))

client = MockBQClient()

# ---------------------------------------------------------
# 1. Basic Aggregation (Mean Mass by Species)
# ---------------------------------------------------------
sql1 = """
SELECT 
    species, 
    AVG(body_mass_g) as avg_mass 
FROM `my-project.dataset.penguins` 
GROUP BY species
"""
df1 = client.query(sql1).to_dataframe()
print("\n--- Average Body Mass by Species ---")
print(df1)

# ---------------------------------------------------------
# 2. Multiple Aggregations
# ---------------------------------------------------------
sql2 = """
SELECT 
    species, 
    COUNT(*) as count,
    AVG(body_mass_g) as mean,
    MIN(body_mass_g) as min,
    MAX(body_mass_g) as max
FROM `my-project.dataset.penguins` 
GROUP BY species
"""
df2 = client.query(sql2).to_dataframe()
print("\n--- Summary Statistics by Species ---")
print(df2)

# ---------------------------------------------------------
# 3. Grouping by Multiple Columns
# ---------------------------------------------------------
sql3 = """
SELECT 
    species, 
    island, 
    AVG(bill_length_mm) as avg_bill
FROM `my-project.dataset.penguins` 
GROUP BY species, island
ORDER BY avg_bill DESC
"""
df3 = client.query(sql3).to_dataframe()
print("\n--- Average Bill Length (Species + Island) ---")
print(df3)
# </transform_aggregate_bigquery>
