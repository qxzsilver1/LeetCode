import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    dist = employee.drop_duplicates(subset= 'salary')
    dist['rnk'] = dist['salary'].rank(method= 'dense', ascending= False)

    res = dist[dist.rnk == N][['salary']]

    if not len(res):
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    
    res = res.rename(columns= {'salary' : f'getNthHighestSalary({N})'})

    return res
