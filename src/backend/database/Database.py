from sqlalchemy import create_engine
import os 
from dotenv import load_dotenv
load_dotenv

connection_string = os.getenv('DATABASE_URL')

engine = create_engine(connection_string)
connection = engine.connect()

# Base = declarative_base()