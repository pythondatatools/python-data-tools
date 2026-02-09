# <load_database_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
# ]
# ///
import duckdb
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

# 2. Main: Read from Database
# DuckDB can query SQLite files directly without importing!
# This is "zero-copy" - it reads the file format directly.

# Install/Load sqlite extension (handled automatically by modern DuckDB, but good to know)
duckdb.sql("INSTALL sqlite; LOAD sqlite;")

# Query directly
query = f"SELECT * FROM sqlite_scan('{db_path}', 'employees')"
df = duckdb.sql(query).show()

# You can also attach it as a database
print("\n--- Attached Database ---")
duckdb.sql(f"ATTACH '{db_path}' AS mydb (TYPE SQLITE)")
duckdb.sql("SELECT name, salary FROM mydb.employees WHERE salary > 70000").show()

# ---------------------------------------------------------
# PRO TIP: Enterprise Data Federation
# ---------------------------------------------------------
# PostgreSQL
# duckdb.sql("INSTALL postgres; LOAD postgres;")
# duckdb.sql("ATTACH 'dbname=mydb user=user password=pass host=localhost' AS my_pg (TYPE POSTGRES)")
# duckdb.sql("SELECT * FROM my_pg.employees").show()

# MySQL / MariaDB
# duckdb.sql("INSTALL mysql; LOAD mysql;")
# duckdb.sql("ATTACH 'user=user password=pass database=mydb' AS my_mysql (TYPE MYSQL)")
# duckdb.sql("SELECT * FROM my_mysql.employees").show()
# </load_database_duckdb>
