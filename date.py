import pandas as pd

def load_df(data_name: str) -> pd.DataFrame:
  path = f"nb_datasets/{data_name}"

  df:pd.DataFrame = pd.read_csv(path)

  # ensure sort by date
  df['date'] = pd.to_datetime(df['date'], dayfirst=True, format='%d/%m/%Y')
  df_sorted: pd.DataFrame = df.sort_values(by='date')
  
  return df_sorted

main_df: pd.DataFrame = load_df("CITY_OF_SAN_PEDRO_processed.csv")

# Group by 'barangay' and find the earliest date for each group
earliest_dates = main_df.groupby('barangay_Res')['date'].min()

# Reset index to make it a DataFrame
earliest_dates = earliest_dates.reset_index()

print(earliest_dates['date'].max())
