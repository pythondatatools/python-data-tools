# <transform_join_pandas>
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
# ]
# ///
import pandas as pd

# ---------------------------------------------------------
# Define Datasets
# ---------------------------------------------------------
employees = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [10, 10, 20, 99]  # David has a non-existent dept
})

departments = pd.DataFrame({
    'dept_id': [10, 20, 30],
    'dept_name': ['HR', 'Engineering', 'Marketing'] # Marketing has no employees
})

print("--- Employees ---")
print(employees)
print("\n--- Departments ---")
print(departments)

# ---------------------------------------------------------
# 1. Inner Join (Matched records only)
# ---------------------------------------------------------
inner_join = pd.merge(employees, departments, on='dept_id', how='inner')
print("\n--- Inner Join (how='inner') ---")
print(inner_join)

# ---------------------------------------------------------
# 2. Left Join (All employees, even without a department match)
# ---------------------------------------------------------
left_join = pd.merge(employees, departments, on='dept_id', how='left')
print("\n--- Left Join (how='left') ---")
print(left_join)

# ---------------------------------------------------------
# 3. Outer Join (All employees and all departments)
# ---------------------------------------------------------
outer_join = pd.merge(employees, departments, on='dept_id', how='outer')
print("\n--- Outer Join (how='outer') ---")
print(outer_join)

# ---------------------------------------------------------
# 4. Right Join (All departments, even if no employees belong to them)
# ---------------------------------------------------------
right_join = pd.merge(employees, departments, on='dept_id', how='right')
print("\n--- Right Join (how='right') ---")
print(right_join)
# </transform_join_pandas>
