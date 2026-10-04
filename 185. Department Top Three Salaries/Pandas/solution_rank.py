import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    top_salaries_df = employee[employee.groupby('departmentId').salary.rank(method= 'dense', ascending= False) <= 3]

    empl_dept_df = top_salaries_df.merge(department, left_on= 'departmentId', right_on= 'id')[['name_y', 'name_x', 'salary']]

    return empl_dept_df.rename(columns= {'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
