from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("root")
password = os.getenv("")
host = os.getenv("127.0.0.1")
database = os.getenv("ventas")

DATABASE_CONNECTION_URI = f"mysql+pymysql://{user}:{password}@{host}/{database}"
