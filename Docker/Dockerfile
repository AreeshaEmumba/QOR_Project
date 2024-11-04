# Use the official Python 3.10 image as a base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt  # Use --no-cache-dir to save space

# Copy the rest of the application files
COPY app /app

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]
