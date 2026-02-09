# <load_database_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
# ]
# ///
import pandas as pd
import sqlite3
import pathlib

# 1. Setup: Ensure database exists (Self-healing)
db_path = "my_database.db"
if not pathlib.Path(db_path).exists():
    print(f"Creating {db_path}...")
    with sqlite3.connect(db_path) as conn:
        # Create dummy data
        df_dummy = pd.DataFrame({
            "id": [1, 2, 3, 4, 5],
            "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
            "dept": ["HR", "IT", "IT", "Finance", "HR"],
            "salary": [60000, 80000, 75000, 90000, 62000]
        })
        df_dummy.to_sql("employees", conn, index=False)

# 2. Main: Read from Database
# Use a context manager to ensure connection closes
with sqlite3.connect(db_path) as conn:
    # Read entire table
    df = pd.read_sql("SELECT * FROM employees", conn)
    print("--- All Employees ---")
    print(df.head())
    
    # Read with filter query
    query = "SELECT name, salary FROM employees WHERE dept = 'IT'"
    df_it = pd.read_sql(query, conn)
    print("\n--- IT Department ---")
    print(df_it)

# ---------------------------------------------------------
# PRO TIP: Connecting to Enterprise Databases
# ---------------------------------------------------------
# PostgreSQL (requires psycopg2)
# conn_str = "postgresql://user:password@localhost:5432/mydb"
# df = pd.read_sql("SELECT * FROM employees", conn_str)

# MS SQL Server (requires pyodbc)
# conn_str = "mssql+pyodbc://user:password@server/mydb?driver=ODBC+Driver+17+for+SQL+Server"
# df = pd.read_sql("SELECT * FROM employees", conn_str)

# IBM DB2 (requires ibm_db_sa)
# conn_str = "ibm_db_sa://user:password@host:port/mydb"
# df = pd.read_sql("SELECT * FROM employees", conn_str)
# </load_database_pandas>
