# <transform_join_duckdb>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "duckdb",
#     "pandas",
# ]
# ///
import duckdb
import pandas as pd

# ---------------------------------------------------------
# Define Datasets in Pandas for easy loading into DuckDB
# ---------------------------------------------------------
employees_df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [10, 10, 20, 99]
})

departments_df = pd.DataFrame({
    'dept_id': [10, 20, 30],
    'dept_name': ['HR', 'Engineering', 'Marketing']
})

# Create DuckDB tables
duckdb.sql("CREATE TABLE employees AS SELECT * FROM employees_df")
duckdb.sql("CREATE TABLE departments AS SELECT * FROM departments_df")

print("--- Employees ---")
duckdb.sql("SELECT * FROM employees").show()
print("\n--- Departments ---")
duckdb.sql("SELECT * FROM departments").show()

# ---------------------------------------------------------
# 1. Inner Join
# ---------------------------------------------------------
print("\n--- Inner Join ---")
duckdb.sql("""
    SELECT e.name, d.dept_name
    FROM employees e
    INNER JOIN departments d ON e.dept_id = d.dept_id
""").show()

# ---------------------------------------------------------
# 2. Left Join
# ---------------------------------------------------------
print("\n--- Left Outer Join ---")
duckdb.sql("""
    SELECT e.name, d.dept_name
    FROM employees e
    LEFT JOIN departments d ON e.dept_id = d.dept_id
""").show()

# ---------------------------------------------------------
# 3. Full Join
# ---------------------------------------------------------
print("\n--- Full Outer Join ---")
duckdb.sql("""
    SELECT e.name, d.dept_name
    FROM employees e
    FULL JOIN departments d ON e.dept_id = d.dept_id
""").show()

# ---------------------------------------------------------
# 4. Joining on Multiple Columns (Example)
# ---------------------------------------------------------
# duckdb.sql("... JOIN ... ON a.id = b.id AND a.year = b.year")
# </transform_join_duckdb>
