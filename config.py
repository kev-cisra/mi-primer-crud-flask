from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("sql_user")
password = os.getenv("sql_password")
host = os.getenv("sql_host")
database = os.getenv("sql_db")

database_uri = f'postgresql://{user}:{password}@{host}/{database}'