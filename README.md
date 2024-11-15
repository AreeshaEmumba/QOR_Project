# QOR_Project
## Project Overview
This project parses log files, stores parsed data in a MySQL database, exposes this data through a Flask-based API, and automates the testing and deployment process with Docker and CI/CD. 

The project consists of several parts:
- Parsing Script: Reads and processes log files to generate a fermi.txt file.
- Recording Script: Stores parsed data from fermi.txt into a MySQL database.
- API Script: Exposes data via a Flask API.
- Dockerized Application: Containerizes the entire application with Docker.
- API Testing: Automates API testing and email reports using Postman and Python.
- CI/CD Pipeline: Automates deployment with GitHub Actions, including Slack notifications.

Technologies Used
- Python: For scripting (parsing, recording, API, sending email reports).
- Flask: For building the API.
- MySQL: Database for storing parsed data.
- Docker: Containerization for both the Flask app and MySQL.
- Postman: For automated API testing.
- Newman: For running Postman tests in the CI/CD pipeline.
- GitHub Actions: For CI/CD automation.
- msmtp: For sending email notifications.

## Log File Parsing

### Parsing Script: `parsing.py`

The `parsing.py` script is designed to parse log files generated by the system, extract relevant statistics, and categorize them into different sections. It then saves these statistics to a `fermi.txt` file located in the `qor` folder for each job ID.

### Features:
- Parses the log file to categorize various statistics into the following groups:
  - **Main Stats**
  - **Runtime Analysis Stats**
  - **Geometric Analysis Stats**
  - **Statistical Analysis (multiple subcategories)**
- Saves the parsed data into a `fermi.txt` file in the respective `qor` folder of the job.
- Supports copying the `qor` folder to a predefined rsync directory.

### Usage:

To use the script, you need to run it from the command line with specific arguments. Here's the general syntax for using the script:

```bash
python parsing.py -l <location> -id <job_id> -p [-r]
```
## Database Recording

### Recording Script: `recording.py`

The `recording.py` script is responsible for processing job data and recording it into a MySQL database. It reads the `fermi.txt` files generated by the log parsing script and inserts the corresponding statistics into various database tables. The script handles job metadata, runtime statistics, geometric analysis, and statistical analysis results, organizing them into appropriate database structures.

### Features:
- Reads `fermi.txt` files from job folders.
- Extracts relevant statistics from each file.
- Inserts or updates records in a MySQL database.
- Supports processing of all job folders or a specific job ID.
- Uses SQLAlchemy ORM for database interaction, ensuring ease of use and scalability.
- Configures detailed logging for tracking the process.

### Database Schema:

The script inserts data into multiple related tables:
- **MetaData**: Contains job metadata such as Fermi ID, Fermi Name, and Revision Commit.
- **Main_Stats**: Stores main statistical data for each job.
- **Geometric_Analysis_Stats**: Stores geometric analysis statistics.
- **Runtime_Analysis_Stats**: Stores runtime-related statistics.
- **Statistical_Analysis**: Several sub-tables store statistical analysis data for different parameters.

Each table is linked to the `MetaData` table through the `UniqueKey`, ensuring data integrity and proper relationship between statistics and their associated job metadata.

### Usage:

To use the script, you need to run it from the command line with specific arguments. Here's the general syntax for using the script:

```bash
python recording.py [-id <job_id>]
```
# App Overview

The app is structured into two main directories: **Flask** and **Docker**. 
- **Flask Folder**: The Flask directory contains the Python application to run it locally on your machine, while the Docker directory is used to deploy the application using docker container.
- **Docker Folder**: Runs the app inside a Docker container, ensuring that the app runs in an isolated and consistent environment across different machines.

## Flask Folder

The `Flask` folder contains the `app.py` file and the `templates` folder, which holds the `index.html` template.
  - `app.py`: The main Flask application that handles routing and querying the database.
  - `templates/index.html`: The HTML template that displays the search form and the results from the database queries.
    
### `app.py`
`app.py` is the entry point for the Flask application. It defines the database models using SQLAlchemy, sets up routes, and queries the database based on user input.

#### Key Features:
- **Database Connection**: It connects to a MySQL database using `SQLAlchemy` and `pymysql`.
- **Models**: Several database models (e.g., `MetaData`, `MainStats`, `RuntimeAnalysisStats`, etc.) are defined to represent the tables in the database.
- **Search Logic**: A form is used to collect search criteria (Fermi ID, Fermi Name, Revision Commit), which is then used to query the `MetaData` table. If matching records are found, it retrieves related data from other tables and displays it.
- **Route Handling**: The root route (`/`) handles both GET and POST requests. The user submits the search form, and the server queries the database for matching records. If data is found, it is passed to the `index.html` template for display.

### `templates/index.html`
This file is the HTML template used to render the search form and display the results of the database query.

#### Key Features:
- **Search Form**: Users can input search criteria (Fermi ID, Fermi Name, and Revision Commit) to query the database.
- **Results Display**: Once the data is retrieved from the database, the results are shown in tables for each related database table.

### Running the Application 
Run the application by writing this command in the Flask directory:

```bash
python3 app.py
```

Click the URL where the app is deployed `127.0.0.1:5000`

## Docker Folder

The Docker folder contains files that allow you to containerize the Flask application, ensuring that it runs in a consistent environment regardless of the host system. The Docker setup includes:

  - `app/app.py`: The main Flask application that handles routing and querying the database.
  - `app/templates/index.html`: The HTML template that displays the search form and the results from the database queries.
  - `docker-compose.yml`: The docker-compose file used to build and deploy the app.
  - `Dockerfile`: The Dockerfile is used to build the Docker image.
  - `db_init/emumba_qor_dump.sql`: The database to be used for the app.

### Running the Application in Docker

To run the Flask app in a Docker container, follow these steps:

1. **docker-compose**: In the Docker folder, build the Docker image and deploy it in a container with the following command:

   ```bash
   docker-compose up --build

2. **Go to Deployed App**: Click the URL where the app is deployed `127.0.0.1:5000`

## Running the Postman Collection and Sending Test Results via Email

In your Postman folder, you have the following files:
- `QOR_Project.postman_collection.json`: The Postman collection file that contains the API tests.
- `package.json`: The configuration file for Node.js and the dependencies, including Newman for running the Postman collection.
- `send_email.py`: A Python script that sends the test results via email after running the tests.
- `node_modules/`: The directory where npm packages, including Newman, are installed.

### Steps to Manually Run the Newman Command and Send Email

#### 1. Install Dependencies

Before running the collection, you need to install the necessary Node.js dependencies:

- **Install Node.js**: Ensure that Node.js and npm (Node Package Manager) are installed on your system. You can check by running:
  ```bash
  node -v
  npm -v
  ```
- **Install newman**:
- **Install msmtp and necessary dependencies**:

#### 2. Run the Postman Collection
- **Run the collection**: Run the collection by typing the following command:
```bash
newman run QOR_Project.postman_collection.json -r html reporter-html-export newman_results.html
```

This will run the collection `QOR_Project.postman_collection.json` and save the results as an html file `newman_results.html`.

#### 3. Send the results in email
- **Run the python script**: Run the send_email.py file to send the 
