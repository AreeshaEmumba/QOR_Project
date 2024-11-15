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

# Function to insert stats into a table
def insert_stats(session, table_class, stat_name, stat_value, unique_key):
    logging.info("Inserting stats.")
    try:
        existing_entry = session.query(table_class).filter_by(
            Stat_Name=stat_name, 
            Stat_Value=stat_value, 
            UniqueKey=unique_key
        ).first()
        
        if existing_entry:
            logging.info(f"Entry exists for {stat_name}, {stat_value}, {unique_key}.")
        else:
            stat_entry = table_class(Stat_Name=stat_name, Stat_Value=stat_value, UniqueKey=unique_key)
            session.add(stat_entry)
            session.commit()
            logging.info(f"Inserted new entry for {stat_name}, {stat_value}, {unique_key}.")
    except SQLAlchemyError as e:
        logging.error(f"Error inserting stats: {e}")
        session.rollback()

# Function to insert metadata
def insert_meta(session, file_path):
    logging.info("Inserting metadata.")
    fermi_job_name = fermi_id = revision_commit = None

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if ":" in line:
            match = re.match(r"(\S+)\s*:\s*(\S+)", line)
            if match:
                key, value = match.groups()
                if key == "fermi_job_name":
                    fermi_job_name = value
                elif key == "fermi_id":
                    fermi_id = value
                elif key == "revision_commit":
                    revision_commit = value

    if fermi_job_name and fermi_id and revision_commit:
        try:
            existing_entry = session.query(MetaData).filter_by(
                Fermi_ID=fermi_id, 
                Fermi_Name=fermi_job_name, 
                Revision_Commit=revision_commit
            ).first()

            if existing_entry:
                logging.info("Updating existing metadata entry.")
            else:
                meta_entry = MetaData(
                    Fermi_ID=fermi_id,
                    Fermi_Name=fermi_job_name,
                    Revision_Commit=revision_commit
                )
                session.add(meta_entry)
                session.commit()
                logging.info("Inserted new metadata entry.")
        except SQLAlchemyError as e:
            logging.error(f"Error inserting metadata: {e}")
            session.rollback()

# Process fermi.txt file
def process_fermi_file(file_path, session):
    logging.info(f"Processing file: {file_path}")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_table_class = None
    for line in lines:
        line = line.strip()
        if line.startswith("[") and line.endswith("]"):
            table_name = line[1:-1].strip()
            current_table_class = TABLE_CLASS_MAPPING.get(table_name)
            if not current_table_class:
                logging.warning(f"Table {table_name} not found in mapping.")
            else:
                logging.info(f"Processing table: {table_name}")
        elif ":" in line and current_table_class:
            match = re.match(r"(\S+)\s*:\s*(\S+)", line)
            if match:
                stat_name, stat_value = match.groups()
                insert_stats(session, current_table_class, stat_name, stat_value, unique_key=None)  # Add unique_key

# Process all jobid folders
def process_all_jobid_folders(root_folder):
    logging.info("Processing all job ID folders.")
    engine, session = create_engine_and_session()

    for jobid_folder in os.listdir(root_folder):
        jobid_path = os.path.join(root_folder, jobid_folder)
        if os.path.isdir(jobid_path):
            qor_folder = os.path.join(jobid_path, 'qor')
            fermi_file_path = os.path.join(qor_folder, 'fermi.txt')
            if os.path.isfile(fermi_file_path):
                logging.info(f"Processing file: {fermi_file_path}")
                insert_meta(session, fermi_file_path)
                process_fermi_file(fermi_file_path, session)

    session.close()
    logging.info("Processing complete.")

if __name__ == "__main__":
    root_folder = '/home/emumba/Desktop/Designs'
    process_all_jobid_folders(root_folder)