# <load_database_bigquery>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-cloud-bigquery",
#     "db-dtypes",
#     "pyarrow", 
# ]
# ///
from google.cloud import bigquery
import os

# Note: BigQuery cannot read your local SQLite file.
# In production, you would use "Federated Queries" (EXTERNAL_QUERY) 
# to query a Cloud SQL (Postgres/MySQL) database without moving data.

# Pseudo-code for simulation since we don't have active credentials
print("--- BigQuery Federated Query ---")

sql = """
SELECT * FROM EXTERNAL_QUERY(
    'projects/my-project/locations/us/connections/my-connection',
    'SELECT * FROM employees WHERE dept = "IT"'
);
"""

print(f"Executing Query:\n{sql}")

# In a real environment:
# client = bigquery.Client()
# df = client.query(sql).to_dataframe()
# print(df)

print("\n[Simulation] Result DataFrame:")
print("   id     name dept  salary")
print("0   2      Bob   IT   80000")
print("1   3  Charlie   IT   75000")
# </load_database_bigquery>
