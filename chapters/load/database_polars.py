# <load_database_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
#     "connectorx",
#     "pyarrow", 
# ]
# ///
import polars as pl
import sqlite3
import pathlib

# 1. Setup: Ensure database exists
db_path = "my_database.db"
if not pathlib.Path(db_path).exists():
    print(f"Creating {db_path}...")
    with sqlite3.connect(db_path) as conn:
        conn.execute("CREATE TABLE employees (id INT, name TEXT, dept TEXT, salary INT)")
        conn.execute("INSERT INTO employees VALUES (1, 'Alice', 'HR', 60000)")
        conn.execute("INSERT INTO employees VALUES (2, 'Bob', 'IT', 80000)")
        conn.execute("INSERT INTO employees VALUES (3, 'Charlie', 'IT', 75000)")

# 2. Main: Read from Database
# Polars uses connectorx or adbc for high performance
uri = f"sqlite://{db_path}"

query = "SELECT * FROM employees"
df = pl.read_database_uri(query=query, uri=uri)

print("--- Polars DataFrame ---")
print(df)

# ---------------------------------------------------------
# PRO TIP: Connecting to Enterprise Databases
# ---------------------------------------------------------
# PostgreSQL (High Permance via ConnectorX)
# uri = "postgresql://user:password@localhost:5432/mydb"
# df = pl.read_database_uri("SELECT * FROM employees", uri)

# MS SQL Server (High Performance via ConnectorX)
# uri = "mssql://user:password@server/mydb?driver=ODBC+Driver+17+for+SQL+Server"
# df = pl.read_database_uri("SELECT * FROM employees", uri)

# IBM DB2 (via SQLAlchemy fallback)
# import sqlalchemy
# engine = sqlalchemy.create_engine("ibm_db_sa://user:password@host:port/mydb")
# df = pl.read_database("SELECT * FROM employees", connection=engine)
# </load_database_polars>
