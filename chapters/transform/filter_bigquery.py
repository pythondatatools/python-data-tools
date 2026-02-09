# <transform_filter_bigquery>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-cloud-bigquery",
#     "pandas",
#     "db-dtypes",
# ]
# ///
import unittest.mock as mock
from google.cloud import bigquery
import pandas as pd
import io

# ---------------------------------------------------------
# Mock Setup (Simulating BigQuery)
# ---------------------------------------------------------
# In a real scenario, you would use:
# client = bigquery.Client()

mock_client = mock.MagicMock(spec=bigquery.Client)
print("--- BigQuery Client Initialized (Mock) ---\n")

# Load mock data for results
data = """species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
Adelie,Torgersen,39.1,18.7,181,3750,Male
Adelie,Torgersen,39.5,17.4,186,3800,Female
Adelie,Torgersen,40.3,18.0,195,3250,Female
Adelie,Torgersen,36.7,19.3,193,3450,Female
Adelie,Torgersen,39.3,20.6,190,3650,Male
Chinstrap,Dream,46.5,17.9,192,3500,Female
Gentoo,Biscoe,46.1,13.2,211,4500,Female
"""
df_mock = pd.read_csv(io.StringIO(data))

def mock_query(query):
    print(f"Executing SQL:\n{query}\n")
    
    # We'll just filter the mock dataframe to simulate the query result
    # ensuring the output matches the SQL intent roughly
    
    result = df_mock.copy()
    
    if "species = 'Adelie'" in query and "island = 'Torgersen'" in query:
        result = result[(result['species'] == 'Adelie') & (result['island'] == 'Torgersen')]
    elif "species = 'Adelie'" in query:
        result = result[result['species'] == 'Adelie']
    elif "bill_length_mm > 45" in query:
        result = result[result['bill_length_mm'] > 45]
    elif "island LIKE 'B%'" in query:
        result = result[result['island'].str.startswith('B')]
    
    # Mock row iterator
    mock_job = mock.MagicMock()
    mock_job.to_dataframe.return_value = result.head(3)
    return mock_job

mock_client.query.side_effect = mock_query

# ---------------------------------------------------------
# 1. Basic Filtering (SQL WHERE)
# ---------------------------------------------------------
query = """
    SELECT * 
    FROM `my-project.dataset.penguins`
    WHERE species = 'Adelie'
    LIMIT 3
"""
df = mock_client.query(query).to_dataframe()
print("--- Result ---")
print(df)

# ---------------------------------------------------------
# 2. Multiple Conditions (AND/OR)
# ---------------------------------------------------------
query = """
    SELECT * 
    FROM `my-project.dataset.penguins`
    WHERE species = 'Adelie' AND island = 'Torgersen'
    LIMIT 3
"""
df = mock_client.query(query).to_dataframe()
print("\n--- Result ---")
print(df)

# ---------------------------------------------------------
# 3. Numeric Comparison
# ---------------------------------------------------------
query = """
    SELECT * 
    FROM `my-project.dataset.penguins`
    WHERE bill_length_mm > 45
    LIMIT 3
"""
df = mock_client.query(query).to_dataframe()
print("\n--- Result ---")
print(df)

# ---------------------------------------------------------
# 4. String Matching (LIKE)
# ---------------------------------------------------------
query = """
    SELECT * 
    FROM `my-project.dataset.penguins`
    WHERE island LIKE 'B%'
    LIMIT 3
"""
df = mock_client.query(query).to_dataframe()
print("\n--- Result ---")
print(df)
# </transform_filter_bigquery>
