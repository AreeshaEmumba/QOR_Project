import re
import os
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Database setup
DATABASE_URL = "mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor_new"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

# Read data from the text file
def read_fermi_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def create_table(table_name, fermi_id, fermi_job_name, revision_commit):
    # Creates a table in the database with an auto-incrementing ID column.
    columns_def = [
        Column("id", Integer, primary_key=True, autoincrement=True),  # Auto-incrementing ID
        Column("fermi_id", Integer),  # Link to fermi_id
        Column("fermi_job_name", String(255)),  # fermi_job_name
        Column("revision_commit", String(255)),  # revision_commit
        Column("Stat_Name", String(255), unique=True),  # Ensure Stat_Name is unique
        Column("Stat_Value", String(255))  # Stat_Value will be a string
    ]
    
    table = Table(table_name, metadata, *columns_def, extend_existing=True)
    metadata.create_all(engine)
    return table

def upsert_data(table, data, fermi_id, fermi_job_name, revision_commit):
    for entry in data:
        stat_name = entry['Stat_Name']
        stat_value = entry['Stat_Value']
        
        # Try to find an existing record with the same Stat_Name and fermi_id
        existing_entry = session.query(table).filter_by(Stat_Name=stat_name, fermi_id=fermi_id).first()
        
        if existing_entry:
            # If found, update the Stat_Value using the update() method
            session.query(table).filter_by(Stat_Name=stat_name, fermi_id=fermi_id).update({"Stat_Value": stat_value})
        else:
            # If not found, insert a new record
            insert_statement = table.insert().values(
                Stat_Name=stat_name, 
                Stat_Value=stat_value,
                fermi_id=fermi_id,
                fermi_job_name=fermi_job_name,
                revision_commit=revision_commit
            )
            session.execute(insert_statement)
    
    # Commit the changes to the database
    try:
        session.commit()
    except IntegrityError:
        session.rollback()

def parse_data(data, fermi_id, fermi_job_name, revision_commit):
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
        table = create_table(table_name, fermi_id, fermi_job_name, revision_commit)
        upsert_data(table, data_list, fermi_id, fermi_job_name, revision_commit)

def process_directory(design_directory):
    # Process each jobid directory inside the design directory
    for jobid in os.listdir(design_directory):
        jobid_path = os.path.join(design_directory, jobid)
        
        if os.path.isdir(jobid_path):
            qor_path = os.path.join(jobid_path, "qor", "fermi.txt")
            
            if os.path.exists(qor_path):
                # Read the fermi.txt file
                data = read_fermi_file(qor_path)
                
                # Extract fermi_id, fermi_job_name, and revision_commit from the file
                fermi_id = extract_stat(data, "fermi_id")
                fermi_job_name = extract_stat(data, "fermi_job_name")
                revision_commit = extract_stat(data, "revision_commit")
                
                # Parse the data and insert/update into the database
                parse_data(data, fermi_id, fermi_job_name, revision_commit)

def extract_stat(data, stat_name):
    # Extract a stat from the data (e.g., fermi_id, fermi_job_name, or revision_commit)
    match = re.search(rf"{stat_name}: (.+)", data)
    if match:
        return match.group(1).strip()
    return None

# Process all jobid directories under the design directory
design_directory = "/home/emumba/Desktop/Designs"
process_directory(design_directory)

print("Tables processed and updated.")
session.close()
