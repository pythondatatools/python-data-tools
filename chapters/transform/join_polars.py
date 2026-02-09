# <transform_join_polars>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "polars",
# ]
# ///
import polars as pl

# ---------------------------------------------------------
# Define Datasets
# ---------------------------------------------------------
employees = pl.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [10, 10, 20, 99]
})

departments = pl.DataFrame({
    'dept_id': [10, 20, 30],
    'dept_name': ['HR', 'Engineering', 'Marketing']
})

print("--- Employees ---")
print(employees)
print("\n--- Departments ---")
print(departments)

# ---------------------------------------------------------
# 1. Inner Join
# ---------------------------------------------------------
inner_join = employees.join(departments, on='dept_id', how='inner')
print("\n--- Inner Join (how='inner') ---")
print(inner_join)

# ---------------------------------------------------------
# 2. Left Join
# ---------------------------------------------------------
left_join = employees.join(departments, on='dept_id', how='left')
print("\n--- Left Join (how='left') ---")
print(left_join)

# ---------------------------------------------------------
# 3. Full Outer Join
# ---------------------------------------------------------
# Note: Polars uses how='full'
outer_join = employees.join(departments, on='dept_id', how='full')
print("\n--- Full Outer Join (how='full') ---")
print(outer_join)

# ---------------------------------------------------------
# 4. Anti Join (Polars Special)
# ---------------------------------------------------------
# Find employees who are NOT in any department (or an invalid one)
anti_join = employees.join(departments, on='dept_id', how='anti')
print("\n--- Anti Join (Employees without a valid Dept) ---")
print(anti_join)
# </transform_join_polars>
