import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_counts = person.groupby('email').size().reset_index(name= 'num')

    duplicated_df = email_counts[email_counts['num'] > 1][['email']]

    return duplicated_df
