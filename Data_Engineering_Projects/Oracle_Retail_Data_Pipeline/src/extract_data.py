import pandas as pd

from db_connection import create_db_engine
from validate_data import VALID_TABLES_DUP

engine = create_db_engine()


def extract_table( table_name ):
    table_name = table_name.lower()
    
    if table_name not in VALID_TABLES_DUP:
        raise ValueError(f"Invalid table name: {table_name}")

    pk = VALID_TABLES_DUP[table_name]

    query = f"""
              SELECT *
                FROM {table_name}
              ORDER BY {pk}
            """

    try:
        df = pd.read_sql(query, engine)
    except Exception:
        print(f"Failed to extract table: {table_name}")
        raise
    
    return df


def print_df_info(table_name, df):
    print("="*30)
    print(f"\tTable - {table_name}:")
    print("="*30)
    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print()