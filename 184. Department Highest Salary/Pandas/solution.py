import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    column_names = ['Department', 'Employee', 'Salary']
    
    if employee.empty or department.empty:
        return pd.DataFrame(columns= column_names)
    
    merged_df = employee.merge(department, left_on= 'departmentId', right_on= 'id', suffixes=('_employee', '_dept'))

    highest_salary_df = merged_df.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])

    highest_salary_df.reset_index(drop=True, inplace=True)

    res_df = highest_salary_df[['name_dept', 'name_employee', 'salary']]

    res_df.columns = column_names

    return res_df
