import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries_df = employee['salary'].drop_duplicates()
    
    second_highest_salary = unique_salaries_df.nlargest(2).iloc[-1] if len(unique_salaries_df) >= 2 else None
    
    res_df = pd.DataFrame({ 'SecondHighestSalary' : [second_highest_salary]}) if second_highest_salary is not None else pd.DataFrame({ 'SecondHighestSalary' : [None]})
    
    return res_df
