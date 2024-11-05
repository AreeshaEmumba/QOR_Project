from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import time
from sqlalchemy.exc import OperationalError

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://d2s:d2s_1234@mysql:3306/emumba_qor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

time.sleep(5)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

# Define the model corresponding to table
class JobData(db.Model):
    __tablename__ = 'fermi_stats'  

    id = db.Column(db.Integer, primary_key=True)
    jobid = db.Column(db.Integer)
    job_name = db.Column(db.String(255))
    revision_name = db.Column(db.String(255))
    stat_name = db.Column(db.String(255))
    stat_value = db.Column(db.String(255))

@app.route('/api/data', methods=['GET'])
def get_data():
    jobid = request.args.get('jobid')
    job_name = request.args.get('job_name')
    revision_name = request.args.get('revision_name')

    query = JobData.query

    if jobid:
        query = query.filter(JobData.jobid == jobid)
    if job_name:
        query = query.filter(JobData.job_name == job_name)
    if revision_name:
        query = query.filter(JobData.revision_name == revision_name)

    results = query.all()

    # Convert results to a list of dictionaries
    output = []
    for job in results:
        output.append({
            'id': job.id,
            'jobid': job.jobid,
            'job_name': job.job_name,
            'revision_name': job.revision_name,
            'stat_name': job.stat_name,
            'stat_value': job.stat_value
        })

    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)