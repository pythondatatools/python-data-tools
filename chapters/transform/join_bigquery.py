# <transform_join_bigquery>
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

# ---------------------------------------------------------
# Mock Setup (Simulating BigQuery)
# ---------------------------------------------------------
mock_client = mock.MagicMock(spec=bigquery.Client)
print("--- BigQuery Client Initialized (Mock) ---\n")

# Prepare mock datasets
employees = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [10, 10, 20, 99]
})

departments = pd.DataFrame({
    'dept_id': [10, 20, 30],
    'dept_name': ['HR', 'Engineering', 'Marketing']
})

def mock_query(query):
    query_clean = query.strip().upper()
    print(f"Executing SQL:\n{query}\n")
    
    # Very simple simulation of SQL Join logic
    if "INNER JOIN" in query_clean:
        result = pd.merge(employees, departments, on='dept_id', how='inner')
    elif "LEFT JOIN" in query_clean:
        result = pd.merge(employees, departments, on='dept_id', how='left')
    elif "FULL JOIN" in query_clean or "FULL OUTER JOIN" in query_clean:
        result = pd.merge(employees, departments, on='dept_id', how='outer')
    else:
        result = employees.copy()
    
    # Return mock job with dataframe result
    mock_job = mock.MagicMock()
    mock_job.to_dataframe.return_value = result[['name', 'dept_name']] if 'dept_name' in result.columns else result
    return mock_job

mock_client.query.side_effect = mock_query

# ---------------------------------------------------------
# 1. Inner Join
# ---------------------------------------------------------
query = """
    SELECT e.name, d.dept_name
    FROM `my-project.dataset.employees` e
    INNER JOIN `my-project.dataset.departments` d ON e.dept_id = d.dept_id
"""
df = mock_client.query(query).to_dataframe()
print("--- Result: Inner Join ---")
print(df)

# ---------------------------------------------------------
# 2. Left Join
# ---------------------------------------------------------
query = """
    SELECT e.name, d.dept_name
    FROM `my-project.dataset.employees` e
    LEFT JOIN `my-project.dataset.departments` d ON e.dept_id = d.dept_id
"""
df = mock_client.query(query).to_dataframe()
print("\n--- Result: Left Join ---")
print(df)

# ---------------------------------------------------------
# 3. Full Join
# ---------------------------------------------------------
query = """
    SELECT e.name, d.dept_name
    FROM `my-project.dataset.employees` e
    FULL OUTER JOIN `my-project.dataset.departments` d ON e.dept_id = d.dept_id
"""
df = mock_client.query(query).to_dataframe()
print("\n--- Result: Full Join ---")
print(df)
# </transform_join_bigquery>
