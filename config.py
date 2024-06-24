#from dotenv import load_dotenv
import os

#load_dotenv()

user = 'postgres'
password = '16022004'
host = 'localhost'
port = '5432'
database = 'taller'

DATABASE_CONNECTION_URI = (
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
)



