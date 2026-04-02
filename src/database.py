import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def database_integration(df):
    DB_URL = os.getenv("DB_URL")

    if not DB_URL:
        raise ValueError("Database URL not found in .env file")

    engine = create_engine(DB_URL)

    df.to_sql(
        name="loan_risk_transactions",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data inserted into MySQL")