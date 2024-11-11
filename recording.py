import os
import re
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# Configure logging to overwrite the file each time the script runs
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
# Base class for the SQLAlchemy ORM
Base = declarative_base()

# Function to create the SQLAlchemy engine and session
def create_engine_and_session():
    logging.info("Now in Function create_engine_and_session") 
    engine = create_engine(f"mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor")
    Session = sessionmaker(bind=engine)
    # Create all tables in the database
    Base.metadata.create_all(engine)
    return engine, Session()

# Define each table as a separate class with __tablename__ and columns
class MetaData(Base):
    __tablename__ = 'MetaData'
    UniqueKey = Column(Integer, unique=True, primary_key=True)
    Fermi_ID = Column(Integer)
    Fermi_Name = Column(String(150))
    Revision_Commit = Column(String(150))

class Main_Stats(Base):
    __tablename__ = 'Main_Stats'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Stat_Name = Column(String(50))
    Stat_Value = Column(String(50))
    UniqueKey = Column(Integer, ForeignKey('MetaData.UniqueKey'))
    meta = relationship("MetaData", backref="fk_UniqueKey")

class Geometric_Analysis_Stats(Base):
    __tablename__ = 'Geometric_Analysis_Stats'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Stat_Name = Column(String(50))
    Stat_Value = Column(String(50))
    UniqueKey = Column(Integer, ForeignKey('MetaData.UniqueKey'))
    meta = relationship("MetaData", backref="fk_Geo")

class Runtime_Analysis_Stats(Base):
    __tablename__ = 'Runtime_Analysis_Stats'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Stat_Name = Column(String(50))
    Stat_Value = Column(String(50))
    UniqueKey = Column(Integer, ForeignKey('MetaData.UniqueKey'))
    meta = relationship("MetaData", backref="fk_Runtime")

class Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose(Base):
    __tablename__ = 'Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Stat_Name = Column(String(50))
    Stat_Value = Column(String(50))
    UniqueKey = Column(Integer, ForeignKey('MetaData.UniqueKey'))
    meta = relationship("MetaData", backref="fk_Negdose")

class Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus(Base):
    __tablename__ = 'Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Stat_Name = Column(String(50))
    Stat_Value = Column(String(50))
    UniqueKey = Column(Integer, ForeignKey('MetaData.UniqueKey'))
    meta = relationship("MetaData", backref="fk_Negfocus")

class Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose(Base):
    __tablename__ = 'Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Stat_Name = Column(String(50))
    Stat_Value = Column(String(50))
    UniqueKey = Column(Integer, ForeignKey('MetaData.UniqueKey'))
    meta = relationship("MetaData", backref="fk_Posdose")

class Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus(Base):
    __tablename__ = 'Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Stat_Name = Column(String(50))
    Stat_Value = Column(String(50))
    UniqueKey = Column(Integer, ForeignKey('MetaData.UniqueKey'))
    meta = relationship("MetaData", backref="fk_Posfocus")

class Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0(Base):
    __tablename__ = 'Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Stat_Name = Column(String(50))
    Stat_Value = Column(String(50))
    UniqueKey = Column(Integer, ForeignKey('MetaData.UniqueKey'))
    meta = relationship("MetaData", backref="fk_f0d0")

class Statistical_Analysis_Width_of_PV_Band_by_Dose(Base):
    __tablename__ = 'Statistical_Analysis_Width_of_PV_Band_by_Dose'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Stat_Name = Column(String(50))
    Stat_Value = Column(String(50))
    UniqueKey = Column(Integer, ForeignKey('MetaData.UniqueKey'))
    meta = relationship("MetaData", backref="fk_Dose")

class Statistical_Analysis_Width_of_PV_Band_by_Focus(Base):
    __tablename__ = 'Statistical_Analysis_Width_of_PV_Band_by_Focus'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Stat_Name = Column(String(50))
    Stat_Value = Column(String(50))
    UniqueKey = Column(Integer, ForeignKey('MetaData.UniqueKey'))
    meta = relationship("MetaData", backref="fk_Focus")

# Table mapping from the fermi.txt table names to class names
TABLE_CLASS_MAPPING = {
    "Main Stats": Main_Stats,
    "Geometric Analysis Stats": Geometric_Analysis_Stats,
    "Runtime Analysis Stats": Runtime_Analysis_Stats,
    "Statistical Analysis:EPE_Target_vs_Mask_Simulation_Negfocus": Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus,
    "Statistical Analysis:EPE_Target_vs_Mask_Simulation_Negdose": Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose,
    "Statistical Analysis:EPE_Target_vs_Mask_Simulation_Posdose": Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose,
    "Statistical Analysis:EPE_Target_vs_Mask_Simulation_Posfocus": Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus,
    "Statistical Analysis:EPE_Target_vs_Nominal_Mask_Simulation_f0d0": Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0,
    "Statistical Analysis:Width_of_PV_Band_by_Dose": Statistical_Analysis_Width_of_PV_Band_by_Dose,
    "Statistical Analysis:Width_of_PV_Band_by_Focus": Statistical_Analysis_Width_of_PV_Band_by_Focus
}


def insert_stats(session, table_class, stat_name, stat_value, unique_key):
    logging.info("Now in Function insert_stats \n")
    try:
        # Check for an existing entry with the same Stat_Name, Stat_Value, and UniqueKey
        existing_entry = session.query(table_class).filter_by(Stat_Name=stat_name, Stat_Value=stat_value, UniqueKey=unique_key).first()
        
        if existing_entry:
            # Optionally, update the existing entry (if needed, otherwise just skip this step)
            logging.info(f"Entry already exists for Stat_Name: {stat_name}, Stat_Value: {stat_value}, UniqueKey: {unique_key}")
        else:
            # Insert a new entry if none found
            stat_entry = table_class(
                Stat_Name=stat_name, 
                Stat_Value=stat_value, 
                UniqueKey=unique_key  # Include unique_key to differentiate the entries
            )
            session.add(stat_entry)
            logging.info(f"Inserting new entry for Stat_Name: {stat_name} with Stat_Value: {stat_value}, UniqueKey: {unique_key}")

        # Commit changes
        session.commit()
        
    except SQLAlchemyError as e:
        logging.error(f"Error upserting stats for Stat_Name: {stat_name} - {e}")
        session.rollback()

def insert_meta(session, table_class, file_path):
    logging.info("Now in Function insert_meta \n")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if ":" in line:
            match = re.match(r"(\S+)\s*:\s*(\S+)", line)

            if "fermi_job_name" in line:
                fermi_job_name = match.group(2)
                logging.info(f"fermi_job_name : {fermi_job_name}")
            
            if "fermi_id" in line:
                fermi_id = match.group(2)  
                logging.info(f"fermi_id : {fermi_id}")        

            if "revision_commit" in line:
                revision_commit = match.group(2)
                logging.info(f"revision_commit : {revision_commit}")

    if fermi_job_name and fermi_id and revision_commit:
        logging.info("Value assigned to fermi_job_name, fermi_id  and revision_commit")
        logging.info(f"fermi_job_name : {fermi_job_name}")
        logging.info(f"fermi_id : {fermi_id}")
        logging.info(f"revision_commit : {revision_commit}")

    try:
        # Check for an existing entry with the same 
        existing_entry = session.query(table_class).filter_by(Fermi_ID=fermi_id, Fermi_Name=fermi_job_name, Revision_Commit=revision_commit).first()
        
        if existing_entry:
            # Update the existing entry's 
            existing_entry.Fermi_ID = fermi_id
            existing_entry.Fermi_Job = fermi_job_name
            existing_entry.Revision_Commit = revision_commit
            logging.info(f"Updating existing entry for Fermi ID: {fermi_id}, Fermi_Job: {fermi_job_name}, Revision_Commit: {revision_commit} ")
        else:
            # Insert a new entry if none found
            stat_entry = table_class(
                Fermi_ID=fermi_id,
                Fermi_Name=fermi_job_name,
                Revision_Commit=revision_commit 
            )
            session.add(stat_entry)
            logging.info(f"Inserting new entry for Fermi_ID: {fermi_id} with Fermi_Name: {fermi_job_name}, Revision_Commit: {revision_commit}")

        
        # Commit changes
        session.commit()
        
    except SQLAlchemyError as e:
        logging.error(f"Error upserting stats for Fermi_ID: {fermi_id} with Fermi_Name: {fermi_job_name}, Revision_Commit: {revision_commit} - {e}")
        session.rollback()

# Function to process the fermi.txt file
def process_fermi_file(file_path, session, unique_key):
    logging.info("Now in function process_fermi_file ")
    logging.info(f"file_path = {file_path}")

    logging.info(f"unique_key : {unique_key}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_table_class = None
    for line in lines:
        line = line.strip()

        if line.startswith("[") and line.endswith("]"):
            logging.info("\n Line starts with [")
            table_name = line[1:-1].strip() 
            current_table_class = TABLE_CLASS_MAPPING.get(table_name)
            if not current_table_class:
                logging.info(f"Table {table_name} not found in mapping.")
            else:
                logging.info(f"Table found : {table_name}")

        if ":" in line and current_table_class:
            logging.info("\n Line has : in it \n")
            match = re.match(r"(\S+)\s*:\s*(\S+)", line)
            logging.info(f"match = {match}")

            if match:
                stat_name = match.group(1)
                stat_value = match.group(2)
                logging.info("Value assigned to stat_name and stat_value")
                insert_stats(session, current_table_class, stat_name, stat_value, unique_key)
                logging.info("Inserted Data to table")

# Function to process all jobid folders
def process_all_jobid_folders(root_folder):
    logging.info("Now in Function process_all_jobid_folders ")
    engine, session = create_engine_and_session()

    # Retrieve all UniqueKeys from MetaData
    unique_keys = session.query(MetaData.UniqueKey).all()
    unique_key_index = 0

    for jobid_folder in os.listdir(root_folder):
        jobid_path = os.path.join(root_folder, jobid_folder)
        if os.path.isdir(jobid_path):
            qor_folder = os.path.join(jobid_path, 'qor')
            fermi_file_path = os.path.join(qor_folder, 'fermi.txt')

            if os.path.isfile(fermi_file_path):
                logging.info(f"Processing {fermi_file_path}...")

                # Ensure we have a UniqueKey available
                if unique_key_index < len(unique_keys):
                    unique_key = unique_keys[unique_key_index].UniqueKey
                    unique_key_index += 1
                else:
                    logging.error("No more UniqueKeys available in MetaData.")
                    break

                insert_meta(session, MetaData, fermi_file_path)
                process_fermi_file(fermi_file_path, session, unique_key)
                logging.info(f"Processed {fermi_file_path}...")
                
    session.close()

if __name__ == "__main__":
    root_folder = '/home/emumba/Desktop/Designs'
    process_all_jobid_folders(root_folder)
