## tranforamtion and casting functions
import time
import config
import datetime
import pandas as pd 
from sqlalchemy import create_engine, exc

months = config.MONTHS
postgres = config.POSTGRS_CREDENTIALS
data_cols = config.DATA_COLS
dims = config.DWH_DIMS_FACTS




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

def connect_to_db(postgres_cred):
    
    engine = create_engine(f'postgresql://{postgres["USER"]}:{postgres["PASSWORD"]}@{postgres["HOST"]}:{postgres["PORT"]}/{postgres["db"]}')
    try:
        with engine.connect() as conn:             
            print(f"succefuly connected to {postgres['db']} at host: {postgres['HOST']}")
        return engine
        
    except exc.SQLAlchemyError as e:
        print(f"connection failed !")
        print(f"Error {e}")


def write_df_to_db(df, table_name, engine):
    
    try:
        print(f"start writing data to {table_name}")
        start_time  = time.time() 
        df.to_sql(name = table_name, con = engine, if_exists='append', index=False, method = "multi", chunksize=1000)
        end_time  = time.time() 
        print(f"Data of {len(df)} record Successfully written to the {table_name} table")
        print(f"the proccess toke {end_time - start_time} seconds")
    
    except exc.SQLAlchemyError as e:
        print(f"failed to write data to {table_name} table")
        print(f"Error: {e}")

    except ValueError as ve:
        print(f"ValueError occured during the write process")
        print(f"Error: {ve}")
    
    except Exception as ex:
        print(f"An expected error occured")
        print(f"Error: {ex}")
    

def finalize_things(engine):
    engine.dispose()
    print("engine disposed and connection closed successfully")

