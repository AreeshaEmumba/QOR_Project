import re
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Database setup
DATABASE_URL = "mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

# Read data from the text file
with open("/home/emumba/Desktop/Designs/9871/qor/fermi.txt", "r") as file:
    data = file.read()

def create_table(table_name):
    # Creates a table in the database with an auto-incrementing ID column.
    columns_def = [
        Column("id", Integer, primary_key=True, autoincrement=True),  # Auto-incrementing ID
        Column("Stat_Name", String(255), unique=True),  # Ensure Stat_Name is unique
        Column("Stat_Value", String(255))  # Stat_Value will be a string
    ]
    
    table = Table(table_name, metadata, *columns_def, extend_existing=True)
    metadata.create_all(engine)
    return table

def upsert_data(table, data):
    for entry in data:
        stat_name = entry['Stat_Name']
        stat_value = entry['Stat_Value']
        
        # Try to find an existing record with the same Stat_Name
        existing_entry = session.query(table).filter_by(Stat_Name=stat_name).first()
        
        if existing_entry:
            # If found, update the Stat_Value using the update() method
            session.query(table).filter_by(Stat_Name=stat_name).update({"Stat_Value": stat_value})
        else:
            # If not found, insert a new record
            insert_statement = table.insert().values(Stat_Name=stat_name, Stat_Value=stat_value)
            session.execute(insert_statement)
    
    # Commit the changes to the database
    try:
        session.commit()
    except IntegrityError:
        session.rollback()

def parse_data(data):
    # Parses data, identifies table names, and processes key-value pairs
    sections = re.split(r"\[(.*?)\]\n", data)[1:]
    
    for i in range(0, len(sections), 2):
        table_name = sections[i].strip().replace(":", "_").replace(" ", "_")
        table_data = sections[i + 1].strip()
        
        data_list = []
        
        for line in table_data.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
                # Save Stat_Name and Stat_Value as pairs
                data_list.append({"Stat_Name": key, "Stat_Value": value})
        
        # Create table and upsert data
        table = create_table(table_name)
        upsert_data(table, data_list)

# Parse the data and insert/update into the database
parse_data(data)
print("Tables processed and updated.")
session.close()