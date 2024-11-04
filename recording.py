import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Connection
engine = create_engine('mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor')

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the fermi_stats table with additional job_name and revision columns
class FermiStats(Base):
    __tablename__ = 'fermi_stats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    jobid = Column(Integer, nullable=False)
    job_name = Column(String(255), nullable=False)
    revision_name = Column(String(255), nullable=False)
    stat_name = Column(String(255), nullable=False)
    stat_value = Column(Text, nullable=False)

# Function to create the fermi_stats table if it doesn't exist
def create_table():
    Base.metadata.create_all(engine)
    print("Table fermi_stats created successfully")

# Function to read fermi.txt and insert or update data in the database
def insert_fermi_data(session, jobid, fermi_file):
    job_name = ""
    revision_name = ""

    # First pass: Find "name" and "revision" values
    with open(fermi_file, 'r') as file:
        for line in file:
            if ':' in line:
                stat_name, stat_value = line.split(':', 1)
                stat_name = stat_name.strip().lower()
                stat_value = stat_value.strip()

                # Only fetch values for "name" and "revision"
                if stat_name == "name":
                    job_name = stat_value
                elif stat_name == "revision":
                    revision_name = stat_value

    # Second pass: Insert or update other stats using job_name and revision_name
    with open(fermi_file, 'r') as file:
        for line in file:
            if ':' in line:
                stat_name, stat_value = line.split(':', 1)
                stat_name = stat_name.strip()
                stat_value = stat_value.strip()

                # Skip "name" and "revision" stats for insertion
                if stat_name.lower() in ["name", "revision"]:
                    continue

                # Check if the stat already exists for the jobid, job_name, revision_name, and stat_name
                existing_stat = session.query(FermiStats).filter_by(
                    jobid=jobid,
                    job_name=job_name,
                    revision_name=revision_name,
                    stat_name=stat_name
                ).first()

                if existing_stat:
                    # Update existing stat value
                    existing_stat.stat_value = stat_value
                else:
                    # Create a new FermiStats instance if stat does not exist
                    fermi_stat = FermiStats(
                        jobid=jobid,
                        job_name=job_name,
                        revision_name=revision_name,
                        stat_name=stat_name,
                        stat_value=stat_value
                    )
                    session.add(fermi_stat)

    session.commit()

# Function to traverse directories and record stats
def record_statistics(session, base_directory):
    # Traverse jobid folders
    for jobid in os.listdir(base_directory):
        jobid_path = os.path.join(base_directory, jobid)
        qor_path = os.path.join(jobid_path, 'qor', 'fermi.txt')

        if os.path.isdir(jobid_path) and os.path.isfile(qor_path):
            insert_fermi_data(session, int(jobid), qor_path)
            print(f"Data recorded or updated for jobid: {jobid}")

# Main function to run the script
def main():
    create_table()  # Create the table
    Session = sessionmaker(bind=engine)
    session = Session()  # Create a new session
    base_directory = '/home/emumba/Desktop/Designs'  # Set the path to your design directory
    record_statistics(session, base_directory)  # Record stats from fermi.txt files
    session.close()  # Close the database session

if __name__ == '__main__':
    main()
