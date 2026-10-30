import pandas as pd
import numpy as np

def process_sales_data(file_path):
    df = pd.read_csv(file_path)
    df.drop_duplicates(inplace=True)
    df['Discount'].fillna(0.0, inplace=True)
    df['Sales'].fillna(df['Sales'].median(), inplace=True)
    df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
    
    print("Cleaned Dataset Summary:")
    print(df.describe())
    return df

if __name__ == "__main__":
    process_sales_data('ready_nest_sales.csv')
