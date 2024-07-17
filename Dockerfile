# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a directory for the application code
WORKDIR /app

# Copy the requirements file to the /app directory
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the /app directory
COPY myshopifyapp/  /app/

# Set up the database and create a superuser
RUN python manage.py migrate

# Ensure the SQLite database has the correct permissions
RUN chmod 644 /app/db.sqlite3

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]