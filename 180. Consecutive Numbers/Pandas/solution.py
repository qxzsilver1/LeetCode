import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = (logs[(logs.num == logs.num.shift(1)) & (logs.num == logs.num.shift(2))])

    return logs.iloc[:, [1]].drop_duplicates('num').rename(columns = {'num': 'ConsecutiveNums'})
