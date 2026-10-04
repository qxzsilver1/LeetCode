import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    empl_dept_df = employee.merge(department, left_on= 'departmentId', right_on= 'id').rename(columns= {'name_y' : 'Department'})
    empl_dept_df = empl_dept_df[['Department', 'departmentId', 'salary']].drop_duplicates()

    top_salaries_df = empl_dept_df.groupby(['Department', 'departmentId']).salary.nlargest(3).reset_index()

    df = top_salaries_df.merge(employee, on= ['departmentId', 'salary'])

    return df[['Department', 'name', 'salary']].rename(columns= {'name': 'Employee', 'salary': 'Salary'})
