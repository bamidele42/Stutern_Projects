# import libraries
import pandas as pd
from sqlalchemy import create_engine

# passing column names as argument
columns = [
    "id",
    "name",
    "age",
    "profession",
    "income"]

# Load in the data
data = pd.read_csv("dummy_data.csv", names=columns)

# instantiate sqlarchemy.create_engine object
engine = create_engine("postgresql+psycopg2://postgres:(Geolaw1990)@localhost:5432/demo_db")

# save the data from dataframe to postgres table
data.to_sql("staff_table", engine, index=False) # Always remember to set the index to False
