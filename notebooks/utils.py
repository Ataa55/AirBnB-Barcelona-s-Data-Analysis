## tranforamtion and casting functions
import pandas as pd 

def select_dim(df, dims, dim_name):
    df_dim = df[dims[dim_name]]
    return df_dim

def convert_to_neumeric(df,cols):
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df[cols] = df[cols].fillna(0)
    return df
    
def convert_to_date(df,cols):
    default_date = pd.Timestamp('1900-01-01')
    for col in cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        df[col] = df[col].fillna(default_date)
    return df

def convert_to_string(df, cols):
    df[cols] = df[cols].astype(str).fillna("N/A")
    return df