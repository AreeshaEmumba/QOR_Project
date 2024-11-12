from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import time
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://d2s:d2s_1234@mysql:3306/emumba_qor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
time.sleep(10)
db = SQLAlchemy(app)

# Define models for each table you want to query
class MetaData(db.Model):
    __tablename__ = 'MetaData'
    Fermi_ID = db.Column(db.Integer, primary_key=True)
    Fermi_Name = db.Column(db.String(150))
    Revision_Commit = db.Column(db.String(150))
    UniqueKey = db.Column(db.Integer)

# Table for Main_Stats
class MainStats(db.Model):
    __tablename__ = 'Main_Stats'
    Id = db.Column(db.Integer, primary_key=True)
    Stat_Name = db.Column(db.String(50))  # Changed to 50
    Stat_Value = db.Column(db.String(50))  # Changed to 50
    UniqueKey = db.Column(db.Integer)

# Table for Runtime_Analysis_Stats (already defined above)
class RuntimeAnalysisStats(db.Model):
    __tablename__ = 'Runtime_Analysis_Stats'
    Id = db.Column(db.Integer, primary_key=True)
    Stat_Name = db.Column(db.String(50))  # Changed to 50
    Stat_Value = db.Column(db.String(50))  # Changed to 50
    UniqueKey = db.Column(db.Integer)

class GeometricAnalysisStats(db.Model):
    __tablename__ = 'Geometric_Analysis_Stats'
    Id = db.Column(db.Integer, primary_key=True)
    Stat_Name = db.Column(db.String(50))
    Stat_Value = db.Column(db.String(50))
    UniqueKey = db.Column(db.Integer)

# Table for Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose
class StatisticalAnalysisEPETargetVsMaskSimulationNegdose(db.Model):
    __tablename__ = 'Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negdose'
    Id = db.Column(db.Integer, primary_key=True)
    Stat_Name = db.Column(db.String(50))  # Changed to 50
    Stat_Value = db.Column(db.String(50))  # Changed to 50
    UniqueKey = db.Column(db.Integer)

# Table for Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus
class StatisticalAnalysisEPETargetVsMaskSimulationNegfocus(db.Model):
    __tablename__ = 'Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Negfocus'
    Id = db.Column(db.Integer, primary_key=True)
    Stat_Name = db.Column(db.String(50))  # Changed to 50
    Stat_Value = db.Column(db.String(50))  # Changed to 50
    UniqueKey = db.Column(db.Integer)

# Table for Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose
class StatisticalAnalysisEPETargetVsMaskSimulationPosdose(db.Model):
    __tablename__ = 'Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posdose'
    Id = db.Column(db.Integer, primary_key=True)
    Stat_Name = db.Column(db.String(50))  # Changed to 50
    Stat_Value = db.Column(db.String(50))  # Changed to 50
    UniqueKey = db.Column(db.Integer)

# Table for Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus
class StatisticalAnalysisEPETargetVsMaskSimulationPosfocus(db.Model):
    __tablename__ = 'Statistical_Analysis_EPE_Target_vs_Mask_Simulation_Posfocus'
    Id = db.Column(db.Integer, primary_key=True)
    Stat_Name = db.Column(db.String(50))  # Changed to 50
    Stat_Value = db.Column(db.String(50))  # Changed to 50
    UniqueKey = db.Column(db.Integer)

# Table for Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0
class StatisticalAnalysisEPETargetVsNominalMaskSimulationF0d0(db.Model):
    __tablename__ = 'Statistical_Analysis_EPE_Target_vs_Nominal_Mask_Simulation_f0d0'
    Id = db.Column(db.Integer, primary_key=True)
    Stat_Name = db.Column(db.String(50))  # Changed to 50
    Stat_Value = db.Column(db.String(50))  # Changed to 50
    UniqueKey = db.Column(db.Integer)

# Table for Statistical_Analysis_Width_of_PV_Band_by_Dose
class StatisticalAnalysisWidthOfPVBandByDose(db.Model):
    __tablename__ = 'Statistical_Analysis_Width_of_PV_Band_by_Dose'
    Id = db.Column(db.Integer, primary_key=True)
    Stat_Name = db.Column(db.String(50))  # Changed to 50
    Stat_Value = db.Column(db.String(50))  # Changed to 50
    UniqueKey = db.Column(db.Integer)

# Table for Statistical_Analysis_Width_of_PV_Band_by_Focus
class StatisticalAnalysisWidthOfPVBandByFocus(db.Model):
    __tablename__ = 'Statistical_Analysis_Width_of_PV_Band_by_Focus'
    Id = db.Column(db.Integer, primary_key=True)
    Stat_Name = db.Column(db.String(50))  # Changed to 50
    Stat_Value = db.Column(db.String(50))  # Changed to 50
    UniqueKey = db.Column(db.Integer)

@app.route("/", methods=["GET", "POST"])
def index():
    table_data = {}
    if request.method == "POST":
        # Get the search terms from the individual fields
        search_fermi_id = request.form.get("search_fermi_id")
        search_fermi_name = request.form.get("search_fermi_name")
        search_revision_commit = request.form.get("search_revision_commit")

        # Initialize metadata variable
        metadata = None

        # Check each search term separately
        if search_fermi_id:
            try:
                search_fermi_id_int = int(search_fermi_id)
                metadata = MetaData.query.filter(
                    (MetaData.Fermi_ID == search_fermi_id_int) | 
                    (MetaData.UniqueKey == search_fermi_id_int)
                ).first()
            except ValueError:
                return "Invalid Job ID entered."

        if search_fermi_name and not metadata:
            metadata = MetaData.query.filter(
                (MetaData.Fermi_Name == search_fermi_name) |
                (MetaData.Revision_Commit == search_fermi_name)
            ).first()

        if search_revision_commit and not metadata:
            metadata = MetaData.query.filter(
                (MetaData.Revision_Commit == search_revision_commit)
            ).first()

        if metadata:
            unique_key = metadata.UniqueKey
            fermi_id = metadata.Fermi_ID
            fermi_name = metadata.Fermi_Name
            revision_commit = metadata.Revision_Commit

            # Fetch all tables with the same unique_key
            tables = [
                MainStats,
                RuntimeAnalysisStats,
                GeometricAnalysisStats,
                StatisticalAnalysisEPETargetVsMaskSimulationNegdose,
                StatisticalAnalysisEPETargetVsMaskSimulationNegfocus,
                StatisticalAnalysisEPETargetVsMaskSimulationPosdose,
                StatisticalAnalysisEPETargetVsMaskSimulationPosfocus,
                StatisticalAnalysisEPETargetVsMaskSimulationPosdose,
                StatisticalAnalysisEPETargetVsNominalMaskSimulationF0d0,
                StatisticalAnalysisWidthOfPVBandByDose,
                StatisticalAnalysisWidthOfPVBandByFocus,
            ]
            
            for table in tables:
                data = db.session.query(table.Stat_Name, table.Stat_Value).filter(table.UniqueKey == unique_key).all()
                table_data[table.__tablename__] = data

            # Pass metadata and table data to the template
            return render_template("index.html", 
                                   table_data=table_data, 
                                   fermi_id=fermi_id, 
                                   fermi_name=fermi_name, 
                                   revision_commit=revision_commit)

        else:
            return "No results found."

    return render_template("index.html", table_data=table_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
