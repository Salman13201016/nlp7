import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd

# .env ফাইল থেকে env variables লোড করা
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


try:
    engine = create_engine(connection_string)
    print(engine)

    with engine.connect() as connection:
        print("✅ Successfully connected to the database!")

    query = "SELECT * FROM customer"

    df = pd.read_sql(query, con=engine)

    print(df)

except Exception as e:
    print("Error:", e)
